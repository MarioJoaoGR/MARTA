
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

# Fixture to create a VariableManager instance for testing
@pytest.fixture(scope="module")
def variable_manager():
    loader = DataLoader()  # Create a data loader instance
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')  # Load the inventory
    return VariableManager(loader=loader, inventory=inventory)  # Initialize the VariableManager with default inventory

# Test initialization with default parameters
def test_variable_manager_initialization_with_default():
    loader = DataLoader()  # Create a data loader instance
    variable_manager = VariableManager(loader=loader)  # Initialize the VariableManager with default inventory
    assert isinstance(variable_manager, VariableManager), "Initialization failed: Expected an instance of VariableManager"

# Test initialization with specified loader and inventory
def test_variable_manager_initialization_with_specified():
    loader = DataLoader()  # Create a data loader instance
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')  # Load the inventory
    variable_manager = VariableManager(loader=loader, inventory=inventory)  # Initialize with specified loader and inventory
    assert isinstance(variable_manager, VariableManager), "Initialization failed: Expected an instance of VariableManager"

# Test initialization with version information
def test_variable_manager_initialization_with_version_info():
    loader = DataLoader()  # Create a data loader instance
    inventory = InventoryManager(loader=loader, sources='my_inventory_file.yml')  # Load the inventory
    version_info = {"version": "2.9"}  # Example version information
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=version_info)  # Initialize with version info
    assert isinstance(variable_manager, VariableManager), "Initialization failed: Expected an instance of VariableManager"

# Test getting extra variables
def test_get_extra_vars(variable_manager):
    extra_vars_dict = variable_manager.extra_vars()
    assert isinstance(extra_vars_dict, dict), "Expected a dictionary for extra variables"

# Test setting a new inventory
def test_set_new_inventory(variable_manager):
    new_inventory = {"hosts": ["host1", "host2"], "vars": {"all": {"ansible_connection": "local"}}}
    variable_manager.set_inventory(new_inventory)
    assert variable_manager._inventory == new_inventory, "Inventory was not set correctly"

# Test getting variables for a play, host, and task
def test_get_vars(variable_manager):
    play = {"name": "play1", "hosts": ["host1"], "tasks": [{"name": "task1", "hosts": ["host1"]}]}
    host = "host1"
    task = "task1"
    vars_dict = variable_manager.get_vars(play=play, host=host, task=task)
    assert isinstance(vars_dict, dict), "Expected a dictionary for variables"

# Test clearing facts for a host
def test_clear_facts(variable_manager):
    hostname = "host1"
    variable_manager.clear_facts(hostname)
    assert hostname not in variable_manager._fact_cache, "Facts were not cleared correctly"
