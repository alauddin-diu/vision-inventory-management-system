"""Sample of a broken python file that will be ignored on import."""

from plugin import Vision_IMSPlugin


class BrokenFileIntegrationPlugin(Vision_IMSPlugin):
    """An very broken plugin."""


aaa = bb  # noqa: F821
