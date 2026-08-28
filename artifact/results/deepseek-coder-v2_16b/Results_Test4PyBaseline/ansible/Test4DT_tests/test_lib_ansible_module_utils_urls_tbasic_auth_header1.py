
import pytest
import base64
import sys

def to_bytes(s, errors='surrogate_or_strict'): return s.encode('utf-8') if sys.version_info[0] == 3 else s

# Assuming basic_auth_header function implementation
def basic_auth_header(username, password):
    """Takes a username and password and returns a byte string suitable for
    using as value of an Authorization header to do basic auth.
    """
    return b"Basic %s" % base64.b64encode(to_bytes("%s:%s" % (username, password), errors='surrogate_or_strict'))

# Test cases for basic_auth_header function
def test_basic_auth_header():
    username = "user"
    password = "pass"
    expected_output = b"Basic dXNlcjpwYXNz"
    
    # Call the function and compare with the expected output
    assert basic_auth_header(username, password) == expected_output

def test_basic_auth_header_with_different_credentials():
    username = "testuser"
    password = "testpass"
    expected_output = b"Basic dGVzdHVzZXI6dGVzdHBhc3M="
    
    # Call the function and compare with the expected output
    assert basic_auth_header(username, password) == expected_output

def test_basic_auth_header_with_empty_password():
    username = "user"
    password = ""
    expected_output = b"Basic dXNlcjo="
    
    # Call the function and compare with the expected output
    assert basic_auth_header(username, password) == expected_output

def test_basic_auth_header_with_empty_username():
    username = ""
    password = "pass"
    expected_output = b"Basic OjBwYXNz"
    
    # Call the function and compare with the expected output