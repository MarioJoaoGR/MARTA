
import pytest
from ansible.inventory.host import Host

def test_host_creation():
    host = Host(name='localhost', port=22)
    assert host.name == 'localhost'
    assert host.vars['ansible_port'] == 22

def test_setting_variable():
    host = Host(name='localhost', port=22)
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'


def test_host_inequality():
    host1 = Host(name='localhost', port=22)
    host2 = Host(name='remotehost', port=22)
    assert host1 != host2