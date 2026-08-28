
import pytest
from ansible.inventory.host import Host


def test_host_with_port():
    host = Host(name='exampleHost', port=22)
    assert host.vars['ansible_port'] == 22


def test_setting_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'