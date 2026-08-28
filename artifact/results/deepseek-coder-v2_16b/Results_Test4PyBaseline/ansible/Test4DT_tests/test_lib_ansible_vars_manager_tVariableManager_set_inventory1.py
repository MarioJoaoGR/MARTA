
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
def test_variable_manager_initialization(variable_manager):
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict)
    assert isinstance(variable_manager._vars_cache, defaultdict)
    assert isinstance(variable_manager._extra_vars, dict), f"Expected _extra_vars to be a dictionary but got {type(variable_manager._extra_vars)}"
    # Ensure the inventory is set correctly