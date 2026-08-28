
import pytest
from ansible.inventory.group import Group

# Test for invalid name input
def test_invalid_name():
    with pytest.raises(TypeError):
        Group(name=123)  # Passing an integer instead of a string should raise TypeError

# Test for invalid input type

# Test for clearing hosts cache
def test_clear_hosts_cache():
    group = Group("valid-group-name")
    assert hasattr(group, '_hosts_cache')  # Initially, _hosts_cache should be present
    
    group.clear_hosts_cache()
    assert group._hosts_cache is None  # After clearing, _hosts_cache should be None

# Test for adding a host to the group
def test_add_host():
    group = Group("valid-group-name")
    host = {"host": "server1", "vars": {"ansible_user": "admin"}}
    
    group.hosts.append(host)  # Adding a host directly, should not raise error
    assert len(group.hosts) == 1  # Ensure the host was added correctly

# Test for adding a child group to the parent group
def test_add_child_group():
    parent_group = Group("parent-group")
    child_group = Group("child-group")
    
    parent_group.child_groups.append(child_group)  # Adding a child group, should not raise error
    assert len(parent_group.child_groups) == 1  # Ensure the child group was added correctly

# Test for setting and getting variables in the group
def test_set_and_get_vars():
    group = Group("valid-group-name")
    group.set_variable('environment', 'production')
    
    vars_copy = group.get_vars()  # Getting the variables, should return a dictionary
    assert vars_copy == {'environment': 'production'}  # Ensure the variable was set correctly