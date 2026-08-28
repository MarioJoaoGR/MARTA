
# Module: ansible.modules.systemd
import pytest
from ansible.modules.systemd import is_running_service

# Test cases for the function `is_running_service`
def test_is_running_service_active():
    status = {'ActiveState': 'active'}
    assert is_running_service(status) == True, "Expected True when ActiveState is 'active'"

def test_is_running_service_activating():
    status = {'ActiveState': 'activating'}
    assert is_running_service(status) == True, "Expected True when ActiveState is 'activating'"

def test_is_running_service_inactive():
    status = {'ActiveState': 'inactive'}
    assert is_running_service(status) == False, "Expected False when ActiveState is 'inactive'"

# Additional edge cases to consider:
def test_is_running_service_missing_key():
    with pytest.raises(KeyError):
        status = {}
        is_running_service(status)  # Should raise KeyError because 'ActiveState' key is missing

def test_is_running_service_wrong_value():
    status = {'ActiveState': 'wrong_state'}
    assert is_running_service(status) == False, "Expected False when ActiveState is not 'active' or 'activating'"

# Additional test cases to cover uncovered line 288
def test_is_running_service_none():
    status = {'ActiveState': None}
    assert is_running_service(status) == False, "Expected False when ActiveState is None"

def test_is_running_service_empty_string():
    status = {'ActiveState': ''}
    assert is_running_service(status) == False, "Expected False when ActiveState is an empty string"

def test_is_running_service_whitespace():
    status = {'ActiveState': ' '}
    assert is_running_service(status) == False, "Expected False when ActiveState is a whitespace character"
