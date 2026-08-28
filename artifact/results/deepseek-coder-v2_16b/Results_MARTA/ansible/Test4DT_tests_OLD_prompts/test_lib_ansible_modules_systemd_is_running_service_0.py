
import pytest
from unittest.mock import patch

def is_running_service(service_status):
    return service_status['ActiveState'] in set(['active', 'activating'])

@pytest.fixture
def valid_active():
    return {'ActiveState': 'active'}

@pytest.fixture
def valid_activating():
    return {'ActiveState': 'activating'}

@pytest.fixture
def invalid_inactive():
    return {'ActiveState': 'inactive'}

def test_valid_input_active(valid_active):
    assert is_running_service(valid_active) == True

def test_valid_input_activating(valid_activating):
    assert is_running_service(valid_activating) == True

def test_invalid_input_inactive(invalid_inactive):
    assert is_running_service(invalid_inactive) == False
