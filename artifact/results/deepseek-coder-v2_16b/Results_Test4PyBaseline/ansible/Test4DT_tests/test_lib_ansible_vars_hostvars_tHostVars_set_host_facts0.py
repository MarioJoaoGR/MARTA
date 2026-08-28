# Module: ansible.vars.hostvars
import pytest
from ansible.inventory import Inventory
from ansible.vars import VariableManager
from ansible.parsing.dataloader import DataLoader

# Import the HostVars class from its module
from ansible.vars.hostvars import HostVars

@pytest.fixture
def setup_hostvars():
    inventory = Inventory(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader())
    loader = DataLoader()
    hostvars = HostVars(inventory, variable_manager, loader)
    return hostvars, inventory, variable_manager

def test_initialization():
    hostvars, inventory, variable_manager = setup_hostvars()
    assert isinstance(hostvars._inventory, Inventory)
    assert isinstance(hostvars._variable_manager, VariableManager)
    assert isinstance(hostvars._loader, DataLoader)
    assert hostvars._variable_manager._hostvars is hostvars

def test_set_host_facts():
    hostvars, inventory, variable_manager = setup_hostvars()
    host = 'hostname'
    facts = {'fact1': 'value1', 'fact2': 'value2'}
    hostvars.set_host_facts(host, facts)
    assert variable_manager._hostvars_cache[host] == facts

def test_access_host_variables():
    hostvars, inventory, variable_manager = setup_hostvars()
    # Assuming 'hostname' is in the inventory and has variables set
    host = 'hostname'
    variable_manager.set_host_variable(host, 'varname1', 'value1')
    variable_manager.set_host_variable(host, 'varname2', 'value2')
    assert hostvars[host] == {'varname1': 'value1', 'varname2': 'value2'}
