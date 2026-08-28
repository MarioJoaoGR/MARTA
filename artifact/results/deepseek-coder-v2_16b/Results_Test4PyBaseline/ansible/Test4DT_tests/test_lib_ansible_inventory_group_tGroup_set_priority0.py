
import pytest
from ansible.inventory.group import Group

# Test creating a group with a specific name
def test_group_creation_with_name():
    group = Group("my-group!@#")
    assert group.name == 'my_group__'

# Test creating a group without a specific name
def test_group_creation_without_name():
    group = Group()
    assert group.name == ''

# Test adding hosts to the group
def test_add_hosts_to_group():
    my_group = Group("webservers")
    my_group.hosts.append("host1.example.com")
    my_group.hosts.append({"hostname": "host2.example.com", "vars": {"key": "value"}})
    assert my_group.name == 'webservers'

# Test setting the priority of a group with valid integer
def test_set_priority_with_valid_integer():
    my_group = Group("webservers")
    my_group.set_priority(2)
    assert my_group.priority == 2

# Test setting the priority of a group with invalid type (should not change the priority)
def test_set_priority_with_invalid_type():
    my_group = Group("webservers")
    initial_priority = my_group.priority
    my_group.set_priority("not an integer")
    assert my_group.priority == initial_priority
