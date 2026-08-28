
import pytest
from ansible.module_utils.common.network import to_ipv6_subnet


def test_valid_case_full_ipv6():
    addr = '2001:db8::1'
    expected_output = '2001:db8::'
    assert to_ipv6_subnet(addr) == expected_output, f"Expected {expected_output}, but got {to_ipv6_subnet(addr)}"

def test_valid_case_more_than_four_groups():
    addr = '2001:db8:cafe:deed:1::1'
    expected_output = '2001:db8:cafe:deed::'
    assert to_ipv6_subnet(addr) == expected_output, f"Expected {expected_output}, but got {to_ipv6_subnet(addr)}"