# Module: ansible.module_utils.facts.network.generic_bsd
import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Fixture to create an instance of the class for testing
@pytest.fixture(scope="module")
def generic_bsd():
    return GenericBsdIfconfigNetwork()

# Test case for default options
def test_get_interfaces_info_default_options(generic_bsd):
    interfaces_info, ip_addresses = generic_bsd.get_interfaces_info('/path/to/ifconfig')
    assert isinstance(interfaces_info, dict), "Expected interfaces_info to be a dictionary"
    assert isinstance(ip_addresses, dict), "Expected ip_addresses to be a dictionary"
    assert 'all_ipv4_addresses' in ip_addresses, "Expected all_ipv4_addresses in ip_addresses"
    assert 'all_ipv6_addresses' in ip_addresses, "Expected all_ipv6_addresses in ip_addresses"
    # Add more assertions to validate the content of interfaces_info and ip_addresses if necessary

# Test case for custom options
def test_get_interfaces_info_custom_options(generic_bsd):
    interfaces_info, ip_addresses = generic_bsd.get_interfaces_info('/path/to/ifconfig', '-x')
    assert isinstance(interfaces_info, dict), "Expected interfaces_info to be a dictionary"
    assert isinstance(ip_addresses, dict), "Expected ip_addresses to be a dictionary"
    # Add more assertions to validate the content of interfaces_info and ip_addresses if necessary

# Test case for method chaining example
def test_get_interfaces_info_method_chaining(generic_bsd):
    interfaces_info, ip_addresses = generic_bsd.get_interfaces_info('/path/to/ifconfig', 'custom_options')
    assert isinstance(interfaces_info, dict), "Expected interfaces_info to be a dictionary"
    assert isinstance(ip_addresses, dict), "Expected ip_addresses to be a dictionary"
    # Add more assertions to validate the content of interfaces_info and ip_addresses if necessary
