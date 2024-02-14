"""Test 002 app."""


def test_app(core):
    """Test app version."""
    assert repr(core) == "Python Projeto Base:0.1.0|Testes"
