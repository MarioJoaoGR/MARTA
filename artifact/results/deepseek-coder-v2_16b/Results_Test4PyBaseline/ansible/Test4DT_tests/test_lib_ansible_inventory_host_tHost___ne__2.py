
import pytest
from ansible.inventory.host import Host

# Test creating a Host instance with name and port
def test_host_creation_with_name_and_port():
    host = Host(name='example_host', port=22)
    assert host.name == 'example_host'
    assert host.vars['ansible_port'] == 22