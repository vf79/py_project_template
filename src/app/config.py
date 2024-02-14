"""Config."""

from dynaconf import Dynaconf


class Config:
    """Config class."""

    def __init__(self):
        """Set settings config."""
        self.settings = Dynaconf(
            settings_files=["settings.toml", ".secrets.toml"],
            environments=True,
        )
        self.settings.setenv(self.settings.env)
