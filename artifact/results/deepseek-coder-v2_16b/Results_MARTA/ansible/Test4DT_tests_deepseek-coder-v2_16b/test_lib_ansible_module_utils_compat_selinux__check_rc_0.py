
import pytest
from ansible.module_utils.compat.selinux import _check_rc
import os

def get_errno():
    # Mock function to return a predefined errno value
    return 12345

# Test scenarios
def test_valid_input():
    rc = 0
    assert _check_rc(rc) == rc

def test_negative_input():
    with pytest.raises(OSError):
        rc = -1
        _check_rc(rc)

def test_zero_input():
    rc = 0
    assert _check_rc(rc) == rc
