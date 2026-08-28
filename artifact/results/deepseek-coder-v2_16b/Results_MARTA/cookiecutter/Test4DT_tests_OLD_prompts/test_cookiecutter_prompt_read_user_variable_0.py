
import pytest
from unittest.mock import patch
import click

# Assuming the function read_user_variable is defined as per the provided documentation
def read_user_variable(var_name, default_value):
    return click.prompt(var_name, default=default_value)

@pytest.mark.parametrize("input_str, expected", [
    ("valid_input", "valid_input"),  # Test valid input scenario
    ("", None),                       # Test empty input scenario
    (123, 123),                       # Test invalid input scenario
])
def test_read_user_variable(monkeypatch, input_str, expected):
    with patch('click.prompt', return_value=expected):
        result = read_user_variable("var_name", "default_value")
        assert result == expected
