
import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Test for valid IPv6 address with prefix and scope ID
def test_valid_input_ipv6_address_with_prefix_and_scope():
    self = GenericBsdIfconfigNetwork()
    words = ['inet6', 'fe80::1%eth0', 'prefixlen', '64', 'scopeid', 'lo0']
    current_if = {'ipv4': [], 'ipv6': []}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    self.parse_inet6_line(words, current_if, ips)
    
    assert len(ips['all_ipv6_addresses']) == 1
    assert ips['all_ipv6_addresses'][0] == 'fe80::1'
    assert len(current_if['ipv6']) == 1
    assert current_if['ipv6'][0]['address'] == 'fe80::1'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == 'lo0'

# Test for valid IPv6 address only
def test_valid_input_ipv6_address_only():
    self = GenericBsdIfconfigNetwork()
    words = ['inet6', 'fe80::1%eth0']
    current_if = {'ipv4': [], 'ipv6': []}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    self.parse_inet6_line(words, current_if, ips)
    
    assert len(ips['all_ipv6_addresses']) == 1
    assert ips['all_ipv6_addresses'][0] == 'fe80::1'
    assert len(current_if['ipv6']) == 1
    assert current_if['ipv6'][0]['address'] == 'fe80::1'
    assert not hasattr(current_if['ipv6'][0], 'prefix')
    assert not hasattr(current_if['ipv6'][0], 'scope')

# Test for invalid input where IPv6 address is missing
def test_invalid_input_missing_ipv6_address():
    self = GenericBsdIfconfigNetwork()
    words = ['inet6']
    current_if = {'ipv4': [], 'ipv6': []}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    with pytest.raises(IndexError):
        self.parse_inet6_line(words, current_if, ips)
