
import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Test Scenario 1: Valid Case
def test_valid_case():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = ['ifconfig', 'eth0', 'inet', '192.168.1.100', 'netmask', '255.255.255.0', 'lladdr', '00:1a:2b:3c:4d:5e']
    current_if = {}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    
    generic_bsd.parse_lladdr_line(words, current_if, ips)
    
    assert 'lladdr' in current_if
    assert current_if['lladdr'] == '00:1a:2b:3c:4d:5e'
    assert len(ips['all_ipv4_addresses']) == 0
    assert len(ips['all_ipv6_addresses']) == 0

# Test Scenario 2: Edge Case with None Values
def test_edge_case():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = None
    current_if = None
    ips = None
    
    with pytest.raises(TypeError):
        generic_bsd.parse_lladdr_line(words, current_if, ips)

# Test Scenario 3: Error Case with Invalid Input Types
def test_error_case():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = 123
    current_if = {}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_attributes': []}
    
    with pytest.raises(TypeError):
        generic_bsd.parse_lladdr_line(words, current_if, ips)
