
import pytest
from unittest.mock import patch

def is_deactivating_service(service_status):
    return service_status['ActiveState'] in set(['deactivating'])

@pytest.fixture
def valid_active_state():
    return {'ActiveState': 'deactivating'}

@pytest.fixture
def valid_inactive_state():
    return {'ActiveState': 'active'}

@pytest.fixture
def invalid_input():
    return {}

def test_valid_input_active_state(valid_active_state):
    assert is_deactivating_service(valid_active_state) == True

def test_valid_input_active_state_false(valid_inactive_state):
    assert is_deactivating_service(valid_inactive_state) == False

def test_invalid_input_missing_key(invalid_input):
    with pytest.raises(KeyError):
        is_deactivating_service(invalid_input)
