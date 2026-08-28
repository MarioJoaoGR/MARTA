
import pytest

def is_deactivating_service(service_status):
    return service_status['ActiveState'] in set(['deactivating'])

# Test 1: Valid input - happy path
def test_valid_input_happy_path():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

# Test 2: Missing key
def test_missing_key():
    service_status = {}
    with pytest.raises(KeyError):
        is_deactivating_service(service_status)

# Test 3: Invalid input - None type
def test_invalid_input():
    service_status = None
    with pytest.raises(TypeError):
        is_deactivating_service(service_status)
