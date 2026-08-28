# Module: ansible.vars.hostvars
import pytest
from ansible.inventory import Inventory
from ansible.vars import VariableManager
from ansible.parsing.dataloader import DataLoader

# Import the HostVars class from its module
from ansible.vars.hostvars import HostVars

@pytest.fixture(scope="module")
def hostvars():
    inventory = Inventory(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader())
    loader = DataLoader()
    return HostVars(inventory, variable_manager, loader)

# Test initialization of HostVars
def test_initialization(hostvars):
    assert isinstance(hostvars._inventory, Inventory)
    assert isinstance(hostvars._variable_manager, VariableManager)
    assert isinstance(hostvars._loader, DataLoader)
    assert hostvars._variable_manager._hostvars is hostvars

# Test setting nonpersistent facts
def test_set_nonpersistent_facts(hostvars):
    host = 'hostname'
    facts = {'fact1': 'value1', 'fact2': 'value2'}
    hostvars.set_nonpersistent_facts(host, facts)
    assert hostvars._variable_manager.get_vars(host) == facts

# Test accessing a non-existent host
def test_accessing_nonexistent_host(hostvars):
    with pytest.raises(KeyError):
        hostvars['non_existent_host']

# Test iterating over all hosts
def test_iterating_over_hosts(hostvars):
    assert len(list(hostvars)) > 0

# Test getting the number of hosts
def test_getting_number_of_hosts(hostvars):
    num_hosts = len(hostvars)
    assert isinstance(num_hosts, int) and num_hosts > 0
