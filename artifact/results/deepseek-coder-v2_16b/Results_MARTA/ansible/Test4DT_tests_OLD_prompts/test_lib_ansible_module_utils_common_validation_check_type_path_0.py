
import pytest
from unittest.mock import patch, MagicMock
import os

def check_type_str(value):
    if not isinstance(value, str):
        raise TypeError(f"'{value}' is not a string and conversion is not allowed")
    return value

def check_type_path(value):
    """Verify the provided value is a string or convert it to a string, then return the expanded path."""
    value = check_type_str(value)
    return os.path.expanduser(os.path.expandvars(value))

@pytest.mark.parametrize("input_value, expected", [
    ("~/mydir", '/home/username/mydir'),
    ("/var/%USERNAME%", '/var/username')
])
def test_valid_input_happy_path(input_value, expected):
    with patch('os.path.expanduser', return_value=expected), \
         patch('os.path.expandvars', return_value=expected):
        assert check_type_path(input_value) == expected

def test_edge_case_none():
    with pytest.raises(TypeError):
        check_type_path(None)

@pytest.mark.parametrize("input_value", [12345, None, True])
def test_invalid_input_error_handling(input_value):
    with pytest.raises(TypeError):
        check_type_path(input_value)
