
import pytest
from ansible.module_utils.facts.network.linux import parse_ip_output

# Test for valid standard input
def test_valid_standard_input():
    output = """
inet 192.168.1.1/24 brd 192.168.1.255 scope global dynamic eth0
inet6 fe80::1ff:fe23:4567:89ab/64 scope link 
"""
    parse_ip_output(output)
    assert 'eth0' in interfaces
    assert 'ipv4' in interfaces['eth0']
    assert interfaces['eth0']['ipv4']['address'] == '192.168.1.1'
    assert interfaces['eth0']['ipv4']['broadcast'] == '192.168.1.255'
    assert interfaces['eth0']['ipv4']['netmask'] == '255.255.255.0'
    assert interfaces['eth0']['ipv4']['network'] == '192.168.1.0'

# Test for edge case with None input
def test_edge_case_none_input():
    parse_ip_output(None)
    assert not interfaces

# Test for error handling with invalid IP output string
def test_error_invalid_input():
    output = """
inet 192.168.1.1/24 brd 192.168.1.255 scope global dynamic eth0
invalid data
"""
    with pytest.raises(ValueError):
        parse_ip_output(output)
