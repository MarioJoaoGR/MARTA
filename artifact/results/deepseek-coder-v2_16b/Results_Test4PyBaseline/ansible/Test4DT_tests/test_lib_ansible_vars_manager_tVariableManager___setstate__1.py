
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
import os
from hashlib import sha1
from collections import defaultdict

# Fixture to create a VariableManager instance for testing
@pytest.fixture
def variable_manager():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    return VariableManager(loader=loader, inventory=inventory)

# Test case to check the initialization of VariableManager with default values
def test_variable_manager_initialization(variable_manager):
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict)
    assert isinstance(variable_manager._vars_cache, defaultdict)
    assert isinstance(variable_manager._extra_vars, dict)
    assert isinstance(variable_manager._host_vars_files, defaultdict)
    assert isinstance(variable_manager._group_vars_files, defaultdict)
    assert variable_manager._inventory is not None
    assert variable_manager._loader is not None