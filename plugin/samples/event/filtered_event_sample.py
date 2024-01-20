"""Sample plugin which responds to events."""

import logging

from django.conf import settings

from plugin import Vision_IMSPlugin
from plugin.mixins import EventMixin

logger = logging.getLogger('Vision_IMS')


class FilteredEventPluginSample(EventMixin, Vision_IMSPlugin):
    """A sample plugin which provides supports for triggered events."""

    NAME = "FilteredEventPlugin"
    SLUG = "filteredsampleevent"
    TITLE = "Triggered by test.event only"

    def wants_process_event(self, event):
        """Return whether given event should be processed or not."""
        return event == "test.event"

    def process_event(self, event, *args, **kwargs):
        """Custom event processing."""
        print(f"Processing triggered event: '{event}'")
        print("args:", str(args))
        print("kwargs:", str(kwargs))

        # Issue warning that we can test for
        if settings.PLUGIN_TESTING:
            logger.debug('Event `%s` triggered in sample plugin', event)
