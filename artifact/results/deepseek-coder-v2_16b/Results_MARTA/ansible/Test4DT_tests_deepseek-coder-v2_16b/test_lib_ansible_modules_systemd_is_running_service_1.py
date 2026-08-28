
import pytest
from ansible.modules.systemd import is_running_service

# Scenario 1: Test when service is in 'active' state
def test_valid_input_active():
    service_status = {'ActiveState': 'active'}
    assert is_running_service(service_status) == True

# Scenario 2: Test when service is in 'activating' state
def test_valid_input_activating():
    service_status = {'ActiveState': 'activating'}
    assert is_running_service(service_status) == True

# Scenario 3: Test when service is in 'inactive' state
def test_invalid_input_inactive():
    service_status = {'ActiveState': 'inactive'}
    assert is_running_service(service_status) == False
