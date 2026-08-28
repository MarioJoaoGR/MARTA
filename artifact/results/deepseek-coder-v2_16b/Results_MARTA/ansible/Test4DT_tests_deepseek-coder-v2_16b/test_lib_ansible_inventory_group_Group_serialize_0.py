
import pytest
from ansible.inventory.group import Group
from ansible.inventory.host import Host

# Test initialization with invalid name

# Test adding a host to the group
def test_add_host():
    group = Group("example_group")
    host1 = Host("server1")
    group.hosts.append(host1)
    assert len(group.hosts) == 1
    assert isinstance(group.hosts[0], Host)

# Test removing a host from the group
def test_remove_host():
    group = Group("example_group")
    host1 = Host("server1")
    group.hosts.append(host1)
    assert len(group.hosts) == 1
    group.hosts.remove(host1)
    assert len(group.hosts) == 0