
import pytest
from ansible.module_utils.urls import basic_auth_header
import base64

def to_bytes(s, errors='surrogate_or_strict'):
    return s.encode('utf-8', errors) if isinstance(s, str) else s

# Test case for when both username and password are provided
def test_basic_auth_header():
    auth_header = basic_auth_header("user", "pass")
    assert isinstance(auth_header, bytes), "Expected a byte string"
    expected_output = b'Basic dXNlcjpwYXNz'
    assert auth_header == expected_output, f"Expected {expected_output}, but got {auth_header}"

# Test case for when username is None

# Test case for when password is None