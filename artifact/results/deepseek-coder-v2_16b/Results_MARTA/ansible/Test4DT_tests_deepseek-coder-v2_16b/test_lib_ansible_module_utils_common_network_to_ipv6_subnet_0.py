
import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

def test_valid_case_full_ipv6():
    addr = '2001:db8::1'
    assert to_ipv6_subnet(addr) == '2001:db8::'

def test_valid_case_more_than_four_groups():
    addr = '2001:db8:cafe:deed:1::1'
    assert to_ipv6_subnet(addr) == '2001:db8:cafe:deed::'

def test_valid_case_minimal_ipv6():
    addr = '::1'
    assert to_ipv6_subnet(addr) == '::::'

def test_edge_case_none():
    addr = None
    with pytest.raises(AttributeError):
        to_ipv6_subnet(addr)

def test_edge_case_empty_string():
    addr = ''
    assert to_ipv6_subnet(addr) == '::'

def test_error_case_invalid_input():
    addr = '2001:db8::invalid'
    with pytest.raises(ValueError):
        to_ipv6_subnet(addr)
