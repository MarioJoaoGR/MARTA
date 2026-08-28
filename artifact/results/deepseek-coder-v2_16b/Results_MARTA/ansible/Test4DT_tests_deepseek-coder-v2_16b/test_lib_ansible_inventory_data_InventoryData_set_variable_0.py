
import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture(scope="module")
def inventory():
    return InventoryData()

# Test setting a valid variable for an existing host
def test_valid_input(inventory):
    inventory.add_group('webservers')
    inventory.add_child('all', 'webservers')
    assert inventory.add_child('webservers', 'host1') is True
    inventory.set_variable('host1', 'ansible_host', '192.168.1.100')
    assert inventory.get_hosts()['host1'].get_vars().get('ansible_host') == '192.168.1.100'

# Test raising error when entity does not exist
def test_missing_entity(inventory):
    with pytest.raises(AnsibleError) as excinfo:
        inventory.set_variable('nonexistent', 'ansible_host', '192.168.1.100')
    assert "Could not identify group or host named nonexistent" in str(excinfo.value)

# Test setting a variable with invalid input types
def test_invalid_input(inventory):
    with pytest.raises(TypeError) as excinfo:
        inventory.set_variable('webservers', 123, 'invalid')
    assert "Expected str for entity" in str(excinfo.value)
