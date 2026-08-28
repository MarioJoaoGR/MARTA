
import pytest
from ansible.inventory.group import Group

# Test initialization with a specific name
def test_init_with_name():
    group = Group("my-group!@#")
    assert group.name == 'my_group__'

# Test initialization without a specific name
def test_init_without_name():
    group = Group()
    assert group.name == ''

# Test setting the priority of the group
def test_set_priority():
    my_group = Group("production")
    my_group.set_priority(2)
    assert my_group.priority == 2

# Test setting a custom variable in the group
def test_set_variable():
    my_group = Group("production")
    my_group.set_variable('env', 'prod')
    assert my_group.vars == {'env': 'prod'}

# Test adding a child group to the current group
def test_add_child_group():
    parent_group = Group("parent")
    child_group = Group("child")
    parent_group.child_groups.append(child_group)
    assert len(parent_group.child_groups) == 1

# Test removing a host from the group
def test_remove_host():
    my_group = Group("webservers")
    my_group.hosts.append("host1.example.com")
    my_group.hosts.remove("host1.example.com")
    assert len(my_group.hosts) == 0
