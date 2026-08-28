
import pytest
from ansible.inventory.host import Host


def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin', "Variable should be set correctly"
    
    host.set_variable('ansible_port', 22)
    assert host.vars['ansible_port'] == 22, "Variable should be updated correctly"

def test_hash():
    host1 = Host(name='exampleHost')
    host2 = Host(name='exampleHost')
    host3 = Host(name='anotherHost')
    
    assert hash(host1) == hash(host2), "Hosts with the same name should have the same hash"
    assert hash(host1) != hash(host3), "Hosts with different names should have different hashes"