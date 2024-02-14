"""Config tests."""

import pytest
from src.app.config import Config
from src.app.core import Core

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
run: Run Priority
"""


def pytest_configure(config):
    """Get markers config."""
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(scope="module")
def core():
    """Fixture client."""
    core = Core()
    return core


@pytest.fixture(scope="module")
def settings():
    """Fixture settings."""
    settings = Config().settings
    return settings
