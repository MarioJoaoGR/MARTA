
import os
import pytest
from unittest.mock import patch

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.mark.parametrize("input_str, expected", [
    ("~/Documents", "/root/Documents"),
    ("$USER/Desktop", "admin/Desktop"),
    ("~", "/root")
])
def test_valid_input(input_str, expected):
    with patch.dict(os.environ, {'USER': 'admin', 'HOME': '/root'}):
        assert expand(input_str) == expected
