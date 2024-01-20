"""Sample implementation for IntegrationPlugin."""
from plugin import Vision_IMSPlugin
from plugin.mixins import UrlsMixin


class NoIntegrationPlugin(Vision_IMSPlugin):
    """A basic plugin."""

    NAME = "NoIntegrationPlugin"


class WrongIntegrationPlugin(UrlsMixin, Vision_IMSPlugin):
    """A basic wrong plugin with urls."""

    NAME = "WrongIntegrationPlugin"
