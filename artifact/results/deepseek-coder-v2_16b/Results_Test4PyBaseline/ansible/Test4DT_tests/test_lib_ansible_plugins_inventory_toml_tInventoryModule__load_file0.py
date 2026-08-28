
import pytest
from ansible.plugins.inventory.toml import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleFileNotFound
import toml
import os

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_load_file_valid_file(inventory_module):
    # Create a temporary TOML file for testing
    with open('test.toml', 'w') as f:
        toml.dump({'hosts': {'host1': {}, 'host2': {}}}, f)
    
    try:
        data = inventory_module._load_file('test.toml')
        assert isinstance(data, dict)
        assert 'hosts' in data
        assert len(data['hosts']) == 2
    finally:
        os.remove('test.toml')

def test_load_file_invalid_file(inventory_module):
    with pytest.raises(AnsibleParserError):
        inventory_module._load_file('nonexistent.toml')

def test_load_file_invalid_filename(inventory_module):
    with pytest.raises(AnsibleParserError):
        inventory_module._load_file(None)

def test_load_file_not_found(inventory_module):
    with pytest.raises(AnsibleFileNotFound):
        inventory_module._load_file('nonexistentpath/toml')
