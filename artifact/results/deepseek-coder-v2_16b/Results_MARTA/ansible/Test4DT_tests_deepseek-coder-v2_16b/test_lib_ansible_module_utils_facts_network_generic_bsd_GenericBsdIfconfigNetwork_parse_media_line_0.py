
import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Test 1: Valid input
def test_valid_input():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = ['eth0', 'media', '100baseT', 'IPv4', '192.168.1.100', 'IPv6', '2001:db8::1']
    current_if = {}
    ips = []
    generic_bsd.parse_media_line(words, current_if, ips)
    
    assert current_if == {'media': '100baseT', 'media_select': None, 'media_type': 'IPv4'}
    assert ips == ['192.168.1.100', '2001:db8::1']

# Test 2: Missing media information
def test_missing_media_info():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = ['eth0', 'IPv4', '192.168.1.100', 'IPv6', '2001:db8::1']
    current_if = {}
    ips = []
    generic_bsd.parse_media_line(words, current_if, ips)
    
    assert current_if == {'media': '192.168.1.100', 'media_select': None, 'media_type': 'IPv4'}
    assert ips == ['2001:db8::1']

# Test 3: Invalid input raises exceptions
def test_invalid_input():
    generic_bsd = GenericBsdIfconfigNetwork()
    words = None
    current_if = {}
    ips = []
    
    with pytest.raises(TypeError):
        generic_bsd.parse_media_line(words, current_if, ips)
