
import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork
import subprocess

@pytest.fixture
def sunos_network():
    return SunOSNetwork()

def test_valid_case(sunos_network):
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = sunos_network.get_interfaces_info(ifconfig_path)
    assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
    assert isinstance(ips, dict), "IPs should be a dictionary"
    assert 'all_ipv4_addresses' in ips, "IPv4 addresses list should be present"
    assert 'all_ipv6_addresses' in ips, "IPv6 addresses list should be present"
    # Add more assertions to check the content of interfaces and ips if needed

def test_edge_case(sunos_network):
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = sunos_network.get_interfaces_info(ifconfig_path)
    assert isinstance(interfaces, dict), "Interfaces should be a dictionary"
    assert isinstance(ips, dict), "IPs should be a dictionary"
    # Add more assertions to check the content of interfaces and ips if needed

def test_invalid_input(sunos_network):
    ifconfig_path = 'invalid/path'
    with pytest.raises(ValueError):
        sunos_network.get_interfaces_info(ifconfig_path)
