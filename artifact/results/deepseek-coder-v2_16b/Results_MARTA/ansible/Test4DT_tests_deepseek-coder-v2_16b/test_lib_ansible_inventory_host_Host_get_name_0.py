
import pytest
from ansible.inventory.host import Host

def test_valid_initialization():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22


def test_initialization_with_gen_uuid_false():
    host = Host(name='exampleHost', port=22, gen_uuid=False)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert host._uuid is None