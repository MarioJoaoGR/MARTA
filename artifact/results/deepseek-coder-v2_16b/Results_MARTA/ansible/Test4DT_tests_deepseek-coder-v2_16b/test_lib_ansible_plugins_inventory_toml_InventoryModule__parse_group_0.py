
import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from collections import MutableMapping, MutableSequence

@pytest.fixture(scope="module")
def inventory_module():
    return InventoryModule()

# Test for valid input with complete group data including vars, children, and hosts
def test_valid_input_complete_group(inventory_module):
    inventory_module._parse_group('webservers', {
        'vars': {'port': 80},
        'children': ['dbservers'],
        'hosts': {'server1.example.com': {'ansible_host': '192.168.1.10'}}
    })
    assert inventory_module.inventory.groups['webservers'].vars == {'port': 80}
    assert 'dbservers' in inventory_module.inventory.groups
    assert inventory_module.inventory.groups['webservers'].hosts == {'server1.example.com'}
    assert inventory_module.inventory.groups['webservers'].hostnames == ['server1.example.com']
    assert inventory_module.inventory.groups['webservers'].get_vars('server1.example.com') == {'ansible_host': '192.168.1.10'}

# Test handling group data as None
def test_none_group_data(inventory_module):
    inventory_module._parse_group('loadbalancers', None)
    assert not hasattr(inventory_module.inventory, 'groups') or 'loadbalancers' not in inventory_module.inventory.groups

# Test invalid input where vars is not a dictionary
def test_invalid_input_vars_not_dict(inventory_module):
    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module._parse_group('webservers', {
            'vars': 'not a dict',
            'children': ['dbservers'],
            'hosts': {'server1.example.com': {'ansible_host': '192.168.1.10'}}
        })
    assert "Invalid 'vars' entry for" in str(excinfo.value)
