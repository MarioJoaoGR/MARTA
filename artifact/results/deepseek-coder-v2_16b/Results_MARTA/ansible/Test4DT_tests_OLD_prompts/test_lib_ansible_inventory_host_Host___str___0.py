
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host




def test_set_variable():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    assert host.vars['ansible_user'] == 'admin'

def test_set_multiple_variables():
    host = Host(name='exampleHost')
    host.set_variable('ansible_user', 'admin')
    host.set_variable('ansible_port', 22)
    assert host.vars['ansible_user'] == 'admin'
    assert host.vars['ansible_port'] == 22