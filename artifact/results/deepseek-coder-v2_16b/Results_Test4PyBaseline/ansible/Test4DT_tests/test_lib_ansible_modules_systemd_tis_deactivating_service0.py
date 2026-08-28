
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