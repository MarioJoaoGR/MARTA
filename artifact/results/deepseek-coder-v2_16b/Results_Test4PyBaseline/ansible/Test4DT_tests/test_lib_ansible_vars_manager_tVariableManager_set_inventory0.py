
# Module: ansible.vars.manager
import pytest
from collections import defaultdict
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

# Fixture to create a VariableManager instance for testing
@pytest.fixture
def variable_manager():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    return VariableManager(loader=loader, inventory=inventory)

# Test initialization with basic parameters
def test_variable_manager_initialization():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict)
    assert isinstance(variable_manager._vars_cache, defaultdict)
    assert isinstance(variable_manager._extra_vars, dict), f"Expected _extra_vars to be a dictionary but got {type(variable_manager._extra_vars)}"
    assert variable_manager._inventory == inventory
    assert variable_manager._loader == loader
    assert variable_manager._omit_token is not None

# Test initialization with version information
def test_variable_manager_initialization_with_version_info():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    version_info = {"version": "2.9"}
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=version_info)
    
    assert isinstance(variable_manager._options_vars, dict)