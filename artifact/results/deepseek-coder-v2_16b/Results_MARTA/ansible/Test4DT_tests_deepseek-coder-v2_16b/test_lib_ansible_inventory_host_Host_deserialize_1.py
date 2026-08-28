
import pytest
from ansible.inventory.host import Host

def test_deserialize():
    data = {
        'name': 'exampleHost',
        'vars': {'ansible_user': 'admin'},
        'address': '',
        'uuid': None,
        'implicit': False,
        'groups': []
    }
    
    host = Host()
    host.deserialize(data)
    
    assert host.name == 'exampleHost'
    assert host.vars['ansible_user'] == 'admin'
    assert host.address == ''
    assert host._uuid is None
    assert host.implicit is False
    assert len(host.groups) == 0
