"""Core."""
from app.config import Config


class Core:
    """Core class."""

    def __init__(self):
        """Initialize core class."""
        self.settings = Config().settings
        self.name = self.settings.name
        self.version = self.settings.version
        self.environ = self.settings.ambiente

    def __repr__(self):
        """Repr Core class."""
        return f"{self.name}:{self.version}|{self.environ.capitalize()}"
