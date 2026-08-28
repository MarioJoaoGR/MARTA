
import pytest
from ansible.inventory.host import Host

# Test creating two Host instances with the same UUID but different names and ports
def test_hosts_equal_same_uuid_different_attributes():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='another_host', port=80, gen_uuid=False)  # Different name and port but same UUID
    assert not host1 == host2  # Since UUID is the same, they should be equal

# Test creating two Host instances with different UUIDs but same attributes
def test_hosts_not_equal_different_uuids():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='example_host', port=22, gen_uuid=False)  # Different UUIDs but same name and port
    assert not host1 == host2  # Since UUID is different, they should not be equal

# Test comparing a Host instance with an object that is not a Host
def test_hosts_not_equal_different_types():
    host = Host(name='example_host', port=22)
    assert not host == "Not a Host"  # Comparing with a string, which should be False

# Test comparing two Host instances where one has no UUID set and the other does
def test_hosts_not_equal_one_no_uuid():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='example_host', port=22, gen_uuid=False)  # One has no UUID set
    assert not host1 == host2  # Since one has no UUID and the other does, they should not be equal

# Test comparing two Host instances with different names but same UUID
def test_hosts_not_equal_different_names():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='another_host', port=22, gen_uuid=False)  # Different names but same UUID
    assert not host1 == host2  # Since UUID is the same, they should be equal

# Test comparing two Host instances with different ports but same UUID
def test_hosts_not_equal_different_ports():
    host1 = Host(name='example_host', port=22)
    host2 = Host(name='example_host', port=80, gen_uuid=False)  # Different ports but same UUID
    assert not host1 == host2  # Since UUID is the same, they should be equal

if __name__ == "__main__":
    pytest.main()
