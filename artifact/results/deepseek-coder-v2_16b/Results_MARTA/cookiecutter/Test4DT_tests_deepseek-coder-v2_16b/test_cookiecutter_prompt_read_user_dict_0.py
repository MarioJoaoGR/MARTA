
import pytest
from cookiecutter.prompt import read_user_dict
import click

def test_valid_input():
    var_name = "Enter your data"
    default_value = {"key": "value"}
    mock_input = '{"key": "value"}'
    
    with pytest.raises(OSError):
        read_user_dict(var_name, default_value)

def test_default_case():
    var_name = "Enter your data"
    default_value = {"key": "value"}
    mock_input = ""
    
    with pytest.raises(OSError):
        read_user_dict(var_name, default_value)
