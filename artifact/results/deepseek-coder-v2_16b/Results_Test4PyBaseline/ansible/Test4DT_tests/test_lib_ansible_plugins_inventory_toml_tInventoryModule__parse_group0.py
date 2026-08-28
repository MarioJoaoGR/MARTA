# Module: ansible.plugins.inventory.toml
import pytest
from ansible.plugins.inventory import toml
from collections.abc import MutableMapping, MutableSequence
from ansible.errors import AnsibleParserError

# Assuming self is an instance of InventoryModule
@pytest.fixture
def inventory_module():
    return toml.InventoryModule()

def test_parse_group_with_vars(inventory_module):
    group_data = {
        "vars": {"environment": "production", "version": "2.0"}
    }
    inventory_module._parse_group("webservers", group_data)
    assert inventory_module.inventory.get_group("webservers").get_vars() == {'environment': 'production', 'version': '2.0'}

def test_parse_group_with_children_and_hosts(inventory_module):
    group_data = {
        "children": ["db_backup", "db_reporting"],
        "hosts": {"db1.example.com": {"ansible_host": "192.168.1.10"}, "db2.example.com": {"ansible_host": "192.168.1.11"}}
    }
    inventory_module._parse_group("dbservers", group_data)
    assert set(inventory_module.inventory.get_group("dbservers").get_children()) == {'db_backup', 'db_reporting'}
    assert inventory_module.inventory.get_host("db1.example.com") is not None
    assert inventory_module.inventory.get_host("db2.example.com") is not None

def test_parse_group_without_data(inventory_module):
    inventory_module._parse_group("ungrouped", None)
    assert not inventory_module.inventory.groups

def test_invalid_group_data(inventory_module):
    with pytest.raises(AnsibleParserError):
        group_data = {
            "vars": "not_a_dict",
            "children": ["valid_child"],
            "hosts": {"valid_host": {}}
        }
        inventory_module._parse_group("invalid_group", group_data)
