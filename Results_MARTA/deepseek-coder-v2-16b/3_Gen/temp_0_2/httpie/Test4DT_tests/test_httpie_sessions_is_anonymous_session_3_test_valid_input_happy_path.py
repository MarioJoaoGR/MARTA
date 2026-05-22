
import pytest
from unittest.mock import patch
import os

def is_anonymous_session(session_name: str) -> bool:
    return os.path.sep in session_name

@pytest.mark.parametrize("session_name, expected", [
    ("session123", False),
    ("anon/session456", True),
    ("/home/user/anon/session789", True),
])
def test_valid_input_happy_path(session_name, expected):
    with patch('os.path.sep', '/'):  # Mocking os.path.sep to simulate a path separator
        assert is_anonymous_session(session_name) == expected
