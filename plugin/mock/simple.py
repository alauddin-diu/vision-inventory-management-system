"""Very simple sample plugin"""

from plugin import Vision_IMSPlugin


class SimplePlugin(Vision_IMSPlugin):
    """A very simple plugin."""

    NAME = 'SimplePlugin'
    SLUG = "simple"
