"""Unit tests for task management."""

import os
from datetime import timedelta

from django.conf import settings
from django.core.management import call_command
from django.db.utils import NotSupportedError
from django.test import TestCase
from django.utils import timezone

from django_q.models import Schedule
from error_report.models import Error

import Vision_IMS.tasks
from common.models import Vision_IMSSetting

threshold = timezone.now() - timedelta(days=30)
threshold_low = threshold - timedelta(days=1)


class ScheduledTaskTests(TestCase):
    """Unit tests for scheduled tasks."""

    def get_tasks(self, name):
        """Helper function to get a Schedule object."""
        return Schedule.objects.filter(func=name)

    def test_add_task(self):
        """Ensure that duplicate tasks cannot be added."""
        task = 'Vision_IMS.tasks.heartbeat'

        self.assertEqual(self.get_tasks(task).count(), 0)

        Vision_IMS.tasks.schedule_task(task, schedule_type=Schedule.MINUTES, minutes=10)

        self.assertEqual(self.get_tasks(task).count(), 1)

        t = Schedule.objects.get(func=task)

        self.assertEqual(t.minutes, 10)

        # Attempt to schedule the same task again
        Vision_IMS.tasks.schedule_task(task, schedule_type=Schedule.MINUTES, minutes=5)
        self.assertEqual(self.get_tasks(task).count(), 1)

        # But the 'minutes' should have been updated
        t = Schedule.objects.get(func=task)
        self.assertEqual(t.minutes, 5)


def get_result():
    """Demo function for test_offloading."""
    return 'abc'


class Vision_IMSTaskTests(TestCase):
    """Unit tests for tasks."""

    def test_offloading(self):
        """Test task offloading."""
        # Run with function ref
        Vision_IMS.tasks.offload_task(get_result)

        # Run with string ref
        Vision_IMS.tasks.offload_task('Vision_IMS.test_tasks.get_result')

        # Error runs
        # Malformed taskname
        with self.assertWarnsMessage(UserWarning, "WARNING: 'Vision_IMS' not started - Malformed function path"):
            Vision_IMS.tasks.offload_task('Vision_IMS')

        # Non existent app
        with self.assertWarnsMessage(UserWarning, "WARNING: 'Vision_IMSABC.test_tasks.doesnotmatter' not started - No module named 'Vision_IMSABC.test_tasks'"):
            Vision_IMS.tasks.offload_task('Vision_IMSABC.test_tasks.doesnotmatter')

        # Non existent function
        with self.assertWarnsMessage(UserWarning, "WARNING: 'Vision_IMS.test_tasks.doesnotexsist' not started - No function named 'doesnotexsist'"):
            Vision_IMS.tasks.offload_task('Vision_IMS.test_tasks.doesnotexsist')

    def test_task_hearbeat(self):
        """Test the task heartbeat."""
        Vision_IMS.tasks.offload_task(Vision_IMS.tasks.heartbeat)

    def test_task_delete_successful_tasks(self):
        """Test the task delete_successful_tasks."""
        from django_q.models import Success

        Success.objects.create(name='abc', func='abc', stopped=threshold, started=threshold_low)
        Vision_IMS.tasks.offload_task(Vision_IMS.tasks.delete_successful_tasks)
        results = Success.objects.filter(started__lte=threshold)
        self.assertEqual(len(results), 0)

    def test_task_delete_old_error_logs(self):
        """Test the task delete_old_error_logs."""
        # Create error
        error_obj = Error.objects.create()
        error_obj.when = threshold_low
        error_obj.save()

        # Check that it is not empty
        errors = Error.objects.filter(when__lte=threshold,)
        self.assertNotEqual(len(errors), 0)

        # Run action
        Vision_IMS.tasks.offload_task(Vision_IMS.tasks.delete_old_error_logs)

        # Check that it is empty again
        errors = Error.objects.filter(when__lte=threshold,)
        self.assertEqual(len(errors), 0)

    def test_task_check_for_updates(self):
        """Test the task check_for_updates."""
        # Check that setting should be empty
        self.assertEqual(Vision_IMSSetting.get_setting('_Vision_IMS_LATEST_VERSION'), '')

        # Get new version
        Vision_IMS.tasks.offload_task(Vision_IMS.tasks.check_for_updates)

        # Check that setting is not empty
        response = Vision_IMSSetting.get_setting('_Vision_IMS_LATEST_VERSION')
        self.assertNotEqual(response, '')
        self.assertTrue(bool(response))

    def test_task_check_for_migrations(self):
        """Test the task check_for_migrations."""
        # Update disabled
        Vision_IMS.tasks.check_for_migrations()

        # Update enabled - no migrations
        os.environ['Vision_IMS_AUTO_UPDATE'] = 'True'
        Vision_IMS.tasks.check_for_migrations()

        # Create migration
        self.assertEqual(len(Vision_IMS.tasks.get_migration_plan()), 0)
        call_command('makemigrations', ['Vision_IMS', '--empty'], interactive=False)
        self.assertEqual(len(Vision_IMS.tasks.get_migration_plan()), 1)

        # Run with migrations - catch no foreigner error
        try:
            Vision_IMS.tasks.check_for_migrations()
        except NotSupportedError as e:  # pragma: no cover
            if settings.DATABASES['default']['ENGINE'] != 'django.db.backends.sqlite3':
                raise e

        # Cleanup
        try:
            migration_name = Vision_IMS.tasks.get_migration_plan()[0][0].name + '.py'
            migration_path = settings.BASE_DIR / 'Vision_IMS' / 'migrations' / migration_name
            migration_path.unlink()
        except IndexError:  # pragma: no cover
            pass
