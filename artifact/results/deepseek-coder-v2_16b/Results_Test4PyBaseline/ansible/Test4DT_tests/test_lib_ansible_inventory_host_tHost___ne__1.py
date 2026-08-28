
import pytest
from ansible.inventory.host import Host

# Test creating two hosts with different UUIDs but same name and port (should be considered equal)
def test_compare_hosts_different_uuid():
    host1 = Host(name='same_host', port=22)
    host2 = Host('same_host', port=22, gen_uuid=False)
    assert not (host1 == host2), "Expected hosts with the same name and port but different UUIDs to be considered equal"
    assert host1 != host2, "Expected __ne__ to return True when comparing hosts with different UUIDs"

# Test comparing a host with itself (should always be considered equal)
def test_compare_host_with_itself():
    host = Host(name='self_host', port=22)
    assert host == host, "Expected a host to be equal to itself"
    assert not (host != host), "Expected __ne__ to return False when comparing a host with itself"

# Test comparing a Host instance with another type (should not be considered equal)
def test_compare_host_with_different_type():
    host = Host(name='diff_type_host', port=22)