
import pytest
from unittest.mock import patch
import os

def is_anonymous_session(session_name: str) -> bool:
    return os.path.sep in session_name

# Test case for invalid input error handling
def test_invalid_input_error_handling():
    with patch('os.path.sep', '/'):  # Mocking the path separator
        assert not is_anonymous_session("session123")
        assert is_anonymous_session("anon/session456")
        assert is_anonymous_session("/home/user/anon/session789")
