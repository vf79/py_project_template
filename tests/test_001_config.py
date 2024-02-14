"""Test 001 settings."""

import pytest


@pytest.mark.run
def test_config(settings):
    """Test settings environment settings."""
    settings.setenv("production")
    assert settings.ambiente == "producao"
    settings.setenv("development")
    assert settings.ambiente == "desenvolvimento"
    settings.setenv("testing")
    assert settings.ambiente == "testes"
    assert (
        settings.secret_key_test
        == "AbCdEfGhIjKlMnOpQrStUvXyZaBcDeFgHiJkLmNoPqRsTuVxYz"
    )
