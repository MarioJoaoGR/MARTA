
import pytest
from ansible.inventory.group import Group

# Test initialization with a name
def test_init_with_name():
    group = Group("my-group!@#")
    assert group.name == 'my_group__'

# Test initialization without a name
def test_init_without_name():
    group = Group()
    assert group.name == ''

# Test deserialization from dictionary
def test_deserialize_from_dict():
    data = {
        'name': 'test-group',
        'vars': {'key': 'value'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [{'name': 'parent-group', 'vars': {}, 'depth': 0, 'hosts': []}]
    }
    group = Group()
    group.deserialize(data)
    assert group.name == 'test_group'
    assert group.vars == {'key': 'value'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert [parent.name for parent in group.parent_groups] == ['parent-group']

# Test __setstate__ method with deserialization
def test_setstate_deserializes():
    data = {
        'name': 'test-group',
        'vars': {'key': 'value'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [{'name': 'parent-group', 'vars': {}, 'depth': 0, 'hosts': []}]
    }
    group = Group()
    group.__setstate__(data)
    assert group.name == 'test_group'
    assert group.vars == {'key': 'value'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert [parent.name for parent in group.parent_groups] == ['parent-group']
