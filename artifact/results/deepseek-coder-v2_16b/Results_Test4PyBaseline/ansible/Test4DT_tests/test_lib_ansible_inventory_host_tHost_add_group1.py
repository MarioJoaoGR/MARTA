
import pytest
from ansible.inventory.host import Host

# Test initialization with name and port
def test_host_initialization():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.address == 'example_host'
    assert hasattr(host, 'vars')
    assert hasattr(host, 'groups')
    assert host.vars == {'ansible_port': 22}
    assert host.groups == []
    assert hasattr(host, '_uuid')
    assert host._uuid is not None
    assert host.implicit is False

# Test setting a variable on the host
def test_set_variable():
    host = Host(name='example_host', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars == {'ansible_port': 22, 'ansible_user': 'admin'}

# Test adding a group to the host
def test_add_group():
    class MockGroup:
        def __init__(self, name):
            self.name = name
        
        def get_ancestors(self):
            return []
    
    host = Host(name='example_host', port=22)
    group1 = MockGroup('group1')
    added = host.add_group(group1)
    assert added is True