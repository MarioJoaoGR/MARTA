# Module: ansible.plugins.inventory.yaml
import pytest
from yaml_inventory import InventoryModule
from ansible.errors import AnsibleError, AnsibleParserError
from collections import MutableMapping
from typing import Any, Dict, List, Optional, Union

# Mocking necessary types and methods for testing
class MockInventory:
    def __init__(self):
        self.groups = {}
    
    def add_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = {'vars': {}, 'children': [], 'hosts': {}}
        return group_name
    
    def set_variable(self, group, var, value):
        self.groups[group]['vars'][var] = value
    
    def add_child(self, parent, child):
        if parent not in self.groups:
            raise AnsibleError("Parent group does not exist")
        if child not in self.groups:
            raise AnsibleError("Child group does not exist")
        self.groups[parent]['children'].append(child)
    
    def get_group(self, group_name):
        return self.groups.get(group_name, None)

class MockDisplay:
    def __init__(self):
        self.warnings = []
    
    def warning(self, message):
        self.warnings.append(message)
    
    def vvv(self, message):
        pass

# Mocking necessary types for type hints
string_types = str
NoneType = type(None)

class TestInventoryModule:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.inventory_module = InventoryModule()
        self.inventory_module.inventory = MockInventory()
        self.inventory_module.display = MockDisplay()
    
    def test_parse_group_valid_data(self):
        group_name = self.inventory_module._parse_group('webservers', {'vars': {'port': 80}, 'hosts': ['server1.example.com', 'server2.example.com']})
        assert group_name == 'webservers'
        assert 'webservers' in self.inventory_module.inventory.groups
        assert self.inventory_module.inventory.get_group('webservers')['vars']['port'] == 80
        assert self.inventory_module.inventory.get_group('webservers')['hosts'] == {'server1.example.com': None, 'server2.example.com': None}
    
    def test_parse_group_invalid_data(self):
        invalid_data = None
        group_name = self.inventory_module._parse_group('invalid_group', invalid_data)
        assert group_name is None
        assert 'invalid_group' not in self.inventory_module.inventory.groups
    
    def test_parse_group_empty_key(self):
        group_name = self.inventory_module._parse_group('dbservers', {'children': ['database'], 'vars': {'user': 'admin'}})
        assert group_name == 'dbservers'
        assert 'dbservers' in self.inventory_module.inventory.groups
        assert 'children' not in self.inventory_module.inventory.get_group('dbservers')
    
    def test_parse_group_unexpected_key(self):
        with pytest.raises(AnsibleParserError):
            group_name = self.inventory_module._parse_group('invalid_group', {'unexpected': 'data'})
