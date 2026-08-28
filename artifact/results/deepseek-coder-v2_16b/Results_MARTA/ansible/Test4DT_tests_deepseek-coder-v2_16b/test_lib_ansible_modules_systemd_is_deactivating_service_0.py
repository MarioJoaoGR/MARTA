
import pytest
from ansible.modules.systemd import is_deactivating_service

def test_is_deactivating_service_correct_key():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

