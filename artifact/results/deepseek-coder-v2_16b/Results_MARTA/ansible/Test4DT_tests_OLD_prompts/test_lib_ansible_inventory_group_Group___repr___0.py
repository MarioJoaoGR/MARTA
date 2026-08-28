
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.group import Group


def test_group_creation_with_provided_name():
    with patch('ansible.inventory.group.to_safe_group_name', return_value='sanitized_name'):
        group = Group(name="my-group!name")
        assert group.name == 'sanitized_name'

def test_group_default_priority():
    group = Group()
    assert group.priority == 1

def test_group_set_priority():
    group = Group(name="my-group!name")
    with patch('ansible.inventory.group.to_safe_group_name', return_value='sanitized_name'):
        group.priority = 2
        assert group.priority == 2

def test_group_add_child_group():
    parent_group = Group(name="parent")
    child_group = Group(name="child")
    parent_group.add_child_group(child_group)
    assert len(parent_group.child_groups) == 1
    assert parent_group.child_groups[0].name == 'child'

def test_group_add_host():
    group = Group()
    host_mock = MagicMock()
    host_mock.name = "example.com"
    group.add_host(host_mock)
    assert len(group.hosts) == 1
    assert group.hosts[0].name == 'example.com'

def test_group_set_variable():
    group = Group()
    group.set_variable('key', 'value')
    assert group.vars['key'] == 'value'