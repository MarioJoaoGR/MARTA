
import pytest
from ansible.inventory.group import Group

def test_deserialize():
    data = {
        'name': 'test_group',
        'vars': {'key': 'value'},
        'depth': 1,
        'hosts': [{'host': 'host1', 'vars': {'ansible_user': 'admin'}}],
        'parent_groups': []
    }
    
    group = Group()
    group.deserialize(data)
    
    assert group.name == 'test_group'
    assert group.vars == {'key': 'value'}
    assert group.depth == 1
    assert len(group.hosts) == 1
    assert group.hosts[0]['host'] == 'host1'
    assert group.hosts[0]['vars']['ansible_user'] == 'admin'
    assert not group.parent_groups

def test_deserialize_with_parent_groups():
    parent_data = {
        'name': 'parent_group',
        'vars': {'key': 'value'},
        'depth': 0,
        'hosts': [],
        'parent_groups': []
    }
    
    data = {
        'name': 'child_group',
        'vars': {},
        'depth': 1,
        'hosts': [],
        'parent_groups': [parent_data]
    }
    
    group = Group()
    group.deserialize(data)
    
    assert group.name == 'child_group'
    assert group.vars == {}
    assert group.depth == 1
    assert not group.hosts
    assert len(group.parent_groups) == 1
    assert group.parent_groups[0].name == 'parent_group'
    assert group.parent_groups[0].vars == {'key': 'value'}
    assert group.parent_groups[0].depth == 0
    assert not group.parent_groups[0].hosts
    assert not group.parent_groups[0].parent_groups
