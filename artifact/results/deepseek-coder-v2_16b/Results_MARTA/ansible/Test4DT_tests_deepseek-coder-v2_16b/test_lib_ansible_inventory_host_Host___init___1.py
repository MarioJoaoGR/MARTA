
import pytest
from lib.ansible.inventory.host import Host
from lib.ansible.inventory.group import Group

# Test adding a group to a host

# Test removing a group from a host
def test_removing_group_from_host():
    host = Host(name='exampleHost')
    group1 = Group(name="webservers")
    host.add_group(group1)
    host.remove_group(group1)
    assert "webservers" not in host.groups, f"Expected 'webservers' to be removed from groups but it is still in {host.groups}"