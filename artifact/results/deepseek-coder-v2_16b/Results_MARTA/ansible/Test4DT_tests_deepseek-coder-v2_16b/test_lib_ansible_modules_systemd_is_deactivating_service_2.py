
import pytest
from ansible.modules.systemd import is_deactivating_service

# Test case 1: Service is in 'deactivating' state
def test_is_deactivating_service_true():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

# Test case 2: Service is not in 'deactivating' state
def test_is_deactivating_service_false():
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

# Test case 3: Service status dictionary with incorrect key
def test_is_deactivating_service_key_error():
    service_status = {'Status': 'deactivating'}
    with pytest.raises(KeyError):
        is_deactivating_service(service_status)

# Test case 4: Empty service status dictionary
def test_is_deactivating_service_empty_dict():
    service_status = {}
    with pytest.raises(KeyError):
        is_deactivating_service(service_status)
