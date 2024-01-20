"""Custom management command to cleanup old settings that are not defined anymore."""

import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger('Vision_IMS')


class Command(BaseCommand):
    """Cleanup old (undefined) settings in the database."""

    def handle(self, *args, **kwargs):
        """Cleanup old (undefined) settings in the database."""
        logger.info("Collecting settings")
        from common.models import Vision_IMSSetting, Vision_IMSUserSetting

        # general settings
        db_settings = Vision_IMSSetting.objects.all()
        model_settings = Vision_IMSSetting.SETTINGS

        # check if key exist and delete if not
        for setting in db_settings:
            if setting.key not in model_settings:
                setting.delete()
                logger.info("deleted setting '%s'", setting.key)

        # user settings
        db_settings = Vision_IMSUserSetting.objects.all()
        model_settings = Vision_IMSUserSetting.SETTINGS

        # check if key exist and delete if not
        for setting in db_settings:
            if setting.key not in model_settings:
                setting.delete()
                logger.info("deleted user setting '%s'", setting.key)

        logger.info("checked all settings")
