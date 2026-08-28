
import pytest
from ansible.inventory.data import InventoryData, Host
from ansible.errors import AnsibleError

# Fixture to create a minimal instance of InventoryData for testing
@pytest.fixture
def inventory():
    inv = InventoryData()
    return inv

# Test adding a valid host without specifying a group
def test_valid_input_happy_path(inventory):
    added_host = inventory.add_host('web1')
    assert added_host == 'web1'
    assert 'web1' in inventory.hosts
    assert isinstance(inventory.hosts['web1'], Host)

# Test raising AnsibleError for an invalid or empty host name
def test_invalid_host_error():
    inv = InventoryData()
    with pytest.raises(AnsibleError):
        added_host = inv.add_host('')

# Test adding a host to an existing group
@pytest.fixture
def inventory_with_group():
    inv = InventoryData()
    inv.add_group('webservers')
    return inv

def test_add_to_existing_group(inventory_with_group):
    added_host = inventory_with_group.add_host('web1', group='webservers')
    assert added_host == 'web1'
    assert 'web1' in inventory_with_group.hosts
    assert 'webservers' in inventory_with_group.groups
    assert inventory_with_group.hosts['web1'].get_name() == 'web1'
