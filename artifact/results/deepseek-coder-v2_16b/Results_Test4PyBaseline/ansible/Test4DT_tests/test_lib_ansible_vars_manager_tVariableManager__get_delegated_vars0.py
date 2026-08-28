
# Module: ansible.vars.manager
import pytest
from collections import defaultdict
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.playbook.task import Task
from ansible.inventory.host import Host

# Fixture to create a VariableManager instance for testing
@pytest.fixture(scope="module")
def variable_manager():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')
    return VariableManager(loader=loader, inventory=inventory)

# Test case to check the initialization of VariableManager with default values
def test_variable_manager_initialization(variable_manager):
    assert isinstance(variable_manager._nonpersistent_fact_cache, defaultdict)
    assert isinstance(variable_manager._vars_cache, defaultdict)