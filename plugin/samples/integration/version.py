"""Sample plugin for versioning."""
from plugin import Vision_IMSPlugin


class VersionPlugin(Vision_IMSPlugin):
    """A small version sample."""

    SLUG = "sampleversion"
    NAME = "Sample Version Plugin"
    DESCRIPTION = "A simple plugin which shows how to use the version limits"
    MIN_VERSION = '0.1.0'
    MAX_VERSION = '1.0.0'
