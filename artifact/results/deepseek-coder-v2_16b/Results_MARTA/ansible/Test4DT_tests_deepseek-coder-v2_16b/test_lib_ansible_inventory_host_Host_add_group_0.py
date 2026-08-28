
import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group



def test_add_existing_group():
    host = Host(name='testHost')
    existing_group = Group(name='webservers')
    host.groups.append(existing_group)  # Simulate an existing group
    assert host.add_group(existing_group) is False, "Expected add_group to return False for an already added group"
    assert len(host.groups) == 1, "Expected the host to not have its groups count incremented if it's already in the list"