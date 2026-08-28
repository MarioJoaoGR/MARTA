# Module: ansible.plugins.inventory.ini
import pytest
from ansible.plugins.inventory import ini

# Fixture to create an instance of InventoryModule for testing
@pytest.fixture
def inventory_module():
    inventory_module = ini.InventoryModule()
    return inventory_module

# Test initialization of the InventoryModule class
def test_inventory_module_initialization(inventory_module):
    assert isinstance(inventory_module, ini.InventoryModule)
    assert inventory_module._filename is None
    assert inventory_module.patterns == {}

# Test parsing a valid INI file
@pytest.mark.parametrize("file_content", [
    "[group1]\nhost1\nhost2\n[group1:vars]\nkey=value\n"
])
def test_parse_valid_ini_file(inventory_module, mocker, file_content):
    # Mock the open function to return the file content
    mocker.patch('builtins.open', new_callable=mocker.mock_open, read_data=file_content)
    
    inventory_module._filename = 'dummy_path'
    inventory_module.parse({}, None, 'dummy_path')
    
    assert 'group1' in inventory_module.inventory.groups
    assert 'host1' in inventory_module.inventory.get_hosts('group1')
    assert 'host2' in inventory_module.inventory.get_hosts('group1')
    assert inventory_module.inventory.get_variable('group1', 'key') == 'value'

# Test parsing an invalid INI file with a syntax error
@pytest.mark.parametrize("file_content", [
    "[group1]\nhost1\ninvalid syntax"
])
def test_parse_invalid_ini_file(inventory_module, mocker, file_content):
    # Mock the open function to return the file content
    mocker.patch('builtins.open', new_callable=mocker.mock_open, read_data=file_content)
    
    inventory_module._filename = 'dummy_path'
    with pytest.raises(Exception):
        inventory_module.parse({}, None, 'dummy_path')

# Test parsing an INI file without a [group1:vars] section
@pytest.mark.parametrize("file_content", [
    "[group1]\nhost1\nhost2"
])
def test_parse_ini_without_vars(inventory_module, mocker, file_content):
    # Mock the open function to return the file content
    mocker.patch('builtins.open', new_callable=mocker.mock_open, read_data=file_content)
    
    inventory_module._filename = 'dummy_path'
    inventory_module.parse({}, None, 'dummy_path')
    
    assert 'group1' in inventory_module.inventory.groups
    assert 'host1' in inventory_module.inventory.get_hosts('group1')
    assert 'host2' in inventory_module.inventory.get_hosts('group1')
    with pytest.raises(KeyError):
        inventory_module.inventory.get_variable('group1', 'key')

# Test parsing an INI file without a [group1] section
@pytest.mark.parametrize("file_content", [
    "[group1:vars]\nkey=value"
])
def test_parse_ini_without_group(inventory_module, mocker, file_content):
    # Mock the open function to return the file content
    mocker.patch('builtins.open', new_callable=mocker.mock_open, read_data=file_content)
    
    inventory_module._filename = 'dummy_path'
    with pytest.raises(Exception):
        inventory_module.parse({}, None, 'dummy_path')
