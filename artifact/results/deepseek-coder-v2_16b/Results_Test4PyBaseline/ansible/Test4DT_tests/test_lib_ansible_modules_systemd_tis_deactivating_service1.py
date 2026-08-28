
import pytest
from ansible.modules.systemd import is_deactivating_service

# Test cases for is_deactivating_service function
def test_is_deactivating_service_true():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

def test_is_deactivating_service_false_active():
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

def test_is_deactivating_service_false_inactive():
    service_status = {'ActiveState': 'inactive'}
    assert is_deactivating_service(service_status) == False

# Additional test cases to cover uncovered lines and edge cases
def test_is_deactivating_service_missing_key():
    with pytest.raises(KeyError):
        service_status = {}
        is_deactivating_service(service_status)

def test_is_deactivating_service_incorrect_value():
    service_status = {'ActiveState': 'unknown'}
    assert is_deactivating_service(service_status) == False

# Test case to ensure the function handles incorrect data types gracefully
def test_is_deactivating_service_non_dict_input():
    with pytest.raises(TypeError):
        service_status = "not a dictionary"
        is_deactivating_service(service_status)
