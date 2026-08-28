
import pytest
from ansible.module_utils.urls import basic_auth_header
import base64

def test_invalid_input():
    with pytest.raises(TypeError):
        basic_auth_header()


def test_valid_input():
    username = "user"
    password = "pass"
    expected_output = b"Basic dXNlcjpwYXNz"
    assert basic_auth_header(username, password) == expected_output