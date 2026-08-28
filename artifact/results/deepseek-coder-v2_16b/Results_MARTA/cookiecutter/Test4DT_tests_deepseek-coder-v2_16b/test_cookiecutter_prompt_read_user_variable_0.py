
import pytest
from cookiecutter.prompt import read_user_variable
import click

def test_valid_input():
    # Mocking click.prompt to return a predefined value for testing purposes
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(click, 'prompt', lambda *args, **kwargs: "John Doe")
        result = read_user_variable("Name", "Unknown")
        assert result == "John Doe"

def test_missing_input():
    # Mocking click.prompt to return the default value when no input is provided
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(click, 'prompt', lambda *args, **kwargs: "Unknown")
        result = read_user_variable("Name", "Unknown")
        assert result == "Unknown"

def test_invalid_input():
    # Mocking click.prompt to return a predefined value for testing purposes
    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr(click, 'prompt', lambda *args, **kwargs: "example@example.com")
        result = read_user_variable("Email", "example@example.com")
        assert result == "example@example.com"
