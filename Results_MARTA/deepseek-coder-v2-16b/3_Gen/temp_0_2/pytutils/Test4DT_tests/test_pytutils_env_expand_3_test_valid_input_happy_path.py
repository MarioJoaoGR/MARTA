
import os
import pytest
from unittest.mock import patch

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.mark.parametrize("input_str, expected", [
    ("~/Documents", os.path.expanduser("~/Documents")),
    ("$HOME/Projects", os.path.expandvars("$HOME/Projects")),
    ("~", os.path.expanduser("~"))
])
def test_valid_input_happy_path(input_str, expected):
    with patch('os.path.expandvars') as mock_expandvars:
        with patch('os.path.expanduser') as mock_expanduser:
            mock_expandvars.return_value = input_str
            mock_expanduser.return_value = expected
            assert expand(input_str) == expected
