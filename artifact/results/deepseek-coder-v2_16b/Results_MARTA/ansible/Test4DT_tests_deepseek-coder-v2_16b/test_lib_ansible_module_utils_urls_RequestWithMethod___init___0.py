
import pytest
from ansible.module_utils.urls import RequestWithMethod

def test_invalid_inputs():
    try:
        req = RequestWithMethod('invalid-url', 'GET')
    except ValueError as e:
        assert str(e) == "unknown url type: 'invalid-url'"
