
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host




def test_get_groups():
    host = Host(name='exampleHost', port=22)
    group1 = MagicMock()
    group2 = MagicMock()
    host.add_group(group1)
    host.add_group(group2)
    assert len(host.get_groups()) == 2

def test_get_vars():
    host = Host(name='exampleHost', port=22)
    host.set_variable('ansible_user', 'admin')
    vars_dict = host.get_vars()
    assert vars_dict['ansible_port'] == 22
    assert vars_dict['ansible_user'] == 'admin'