
import pytest
from ansible.inventory.host import Host


def test_create_host_with_name_and_port():
    """Test creating a Host instance with both name and port."""
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22

def test_create_host_with_name_and_uuid():
    """Test creating a Host instance with both name and generating a unique identifier."""
    host = Host(name='exampleHost', port=22, gen_uuid=True)
    assert isinstance(host._uuid, str)

def test_set_variable_for_host():
    """Test setting a variable for the host."""
    host = Host(name='exampleHost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'


