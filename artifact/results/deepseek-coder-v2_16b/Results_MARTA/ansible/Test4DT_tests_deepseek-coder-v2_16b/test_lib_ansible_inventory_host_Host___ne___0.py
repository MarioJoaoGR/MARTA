
import pytest
from ansible.inventory.host import Host

def test_valid_input():
    host = Host(name='validHost', port=22)
    assert host.name == 'validHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host.vars['ansible_port'], int)


def test_uuid_generation():
    host = Host(name='genUUIDHost', gen_uuid=True)
    assert host._uuid is not None
    assert isinstance(host._uuid, str)

def test_no_uuid_generation():
    host = Host(name='noUUIDHost', gen_uuid=False)
    assert host._uuid is None