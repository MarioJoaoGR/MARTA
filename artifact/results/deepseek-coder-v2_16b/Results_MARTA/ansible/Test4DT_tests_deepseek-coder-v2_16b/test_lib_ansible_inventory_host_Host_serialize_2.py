
import pytest
from ansible.inventory.host import Host

# Test scenarios for Host class in Ansible inventory module

def test_valid_input_happy_path():
    host = Host(name='exampleHost', port=22, gen_uuid=True)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str) and len(host._uuid) > 0

def test_edge_case_none_values():
    host = Host(name=None, port=None, gen_uuid=False)
    assert host.name is None
    assert host.address is None
    assert 'ansible_port' not in host.vars
    assert host._uuid is None

def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        host = Host(name='exampleHost', port='not_an_integer')
