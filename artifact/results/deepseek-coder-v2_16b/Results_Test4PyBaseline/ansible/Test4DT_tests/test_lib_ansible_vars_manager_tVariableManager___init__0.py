
# Module: ansible.vars.manager
import pytest
from collections import defaultdict
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

# Test initialization of VariableManager with default parameters
def test_variable_manager_default_init():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict), "Expected _nonpersistent_fact_cache to be a defaultdict"
    assert isinstance(variable_manager._vars_cache, defaultdict), "Expected _vars_cache to be a defaultdict"