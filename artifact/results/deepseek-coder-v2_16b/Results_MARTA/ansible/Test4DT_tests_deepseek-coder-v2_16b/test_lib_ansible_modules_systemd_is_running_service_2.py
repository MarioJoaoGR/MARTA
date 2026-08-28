
import pytest
from ansible.modules.systemd import is_running_service

# Test when service is active
def test_valid_input_active():
    service_status = {'ActiveState': 'active'}
    assert is_running_service(service_status) == True

# Test when service is activating
def test_valid_input_activating():
    service_status = {'ActiveState': 'activating'}
    assert is_running_service(service_status) == True

# Test when service is inactive
def test_invalid_input_inactive():
    service_status = {'ActiveState': 'inactive'}
    assert is_running_service(service_status) == False
