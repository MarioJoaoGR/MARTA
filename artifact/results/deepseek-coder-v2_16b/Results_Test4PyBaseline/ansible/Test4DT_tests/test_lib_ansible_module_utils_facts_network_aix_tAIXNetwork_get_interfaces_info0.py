# Module: ansible.module_utils.facts.network.aix
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.network.aix import AIXNetwork

# Fixture to create an instance of AIXNetwork for testing
@pytest.fixture
def aix_network():
    return AIXNetwork()

# Test case for get_interfaces_info with default options
def test_get_interfaces_info_default(aix_network):
    ifconfig_path = '/usr/sbin/ifconfig'  # Mock or provide the actual path
    interfaces, ips = aix_network.get_interfaces_info(ifconfig_path)
    assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
    assert isinstance(ips, dict), "IPs should be a dictionary"
    assert 'all_ipv4_addresses' in ips, "IPs should contain all IPv4 addresses"
    assert 'all_ipv6_addresses' in ips, "IPs should contain all IPv6 addresses"

# Test case for get_interfaces_info with custom options
def test_get_interfaces_info_custom(aix_network):
    ifconfig_path = '/usr/sbin/ifconfig'  # Mock or provide the actual path
    custom_options = '-x'  # Example custom option
    interfaces, ips = aix_network.get_interfaces_info(ifconfig_path, custom_options)
    assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
    assert isinstance(ips, dict), "IPs should be a dictionary"
    assert 'all_ipv4_addresses' in ips, "IPs should contain all IPv4 addresses"
    assert 'all_ipv6_addresses' in ips, "IPs should contain all IPv6 addresses"

# Test case for get_interfaces_info with different path for ifconfig command
def test_get_interfaces_info_different_path(aix_network):
    custom_ifconfig_path = '/usr/sbin/ifconfig'  # Replace with actual path if different
    interfaces, ips = aix_network.get_interfaces_info(custom_ifconfig_path)
    assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
    assert isinstance(ips, dict), "IPs should be a dictionary"
    assert 'all_ipv4_addresses' in ips, "IPs should contain all IPv4 addresses"
    assert 'all_ipv6_addresses' in ips, "IPs should contain all IPv6 addresses"

# Test case for get_interfaces_info within a larger module or script context
def test_get_interfaces_info_context(aix_network):
    with patch('ansible.module_utils.facts.network.aix.AIXNetwork.module', MagicMock()):
        generic_bsd = GenericBsdIfconfigNetwork()
        interfaces, ips = generic_bsd.get_interfaces_info('/usr/sbin/ifconfig')
        assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
        assert isinstance(ips, dict), "IPs should be a dictionary"
        assert 'all_ipv4_addresses' in ips, "IPs should contain all IPv4 addresses"
        assert 'all_ipv6_addresses' in ips, "IPs should contain all IPv6 addresses"
