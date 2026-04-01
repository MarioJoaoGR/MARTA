
import os
from unittest.mock import patch
import pytest

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.mark.parametrize("input_str, expected", [
    ("~/Documents", os.path.expanduser("~/Documents")),
    ("$HOME/Projects", os.getenv("HOME") + "/Projects"),
    ("~", os.path.expanduser("~"))
])
@patch('os.path.expandvars')
@patch('os.path.expanduser')
def test_valid_input(mock_expanduser, mock_expandvars, input_str, expected):
    # Mock the behavior of expandvars and expanduser to return the expected value
    mock_expandvars.return_value = input_str
    mock_expanduser.return_value = expected
    
    result = expand(input_str)
    assert result == expected
