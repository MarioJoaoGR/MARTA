
import pytest
from ansible.utils.color import hostcolor

# Test cases for the hostcolor function
def test_hostcolor_no_issues():
    assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 0}) == 'localhost'

def test_hostcolor_with_unreachable():
    assert hostcolor("remote_host", {"failures": 1, "unreachable": 2, "changed": 0}, color=False) == 'remote_host'

def test_hostcolor_with_changes():
    assert hostcolor("another_host", {"failures": 0, "unreachable": 0, "changed": 5}) == 'another_host'

def test_hostcolor_default_settings():
    assert hostcolor("default_host", {"failures": 1, "unreachable": 1, "changed": 3}) == 'default_host'
