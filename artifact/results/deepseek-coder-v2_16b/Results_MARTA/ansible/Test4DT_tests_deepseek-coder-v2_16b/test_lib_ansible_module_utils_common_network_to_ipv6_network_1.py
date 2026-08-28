
import pytest
from your_module import to_ipv6_network  # Replace 'your_module' with the actual module name where `to_ipv6_network` is defined.

# Test case for a full IPv6 address
def test_valid_case_full_ipv6():
    addr = '2001:db8::1'
    expected_output = '2001:db8::'
    assert to_ipv6_network(addr) == expected_output

# Test case for an IPv6 address with fewer than three groupings
def test_valid_case_less_than_three_groupings():
    addr = '2001:db8:1:2:3:4:5:6'
    expected_output = '2001:db8::'
    assert to_ipv6_network(addr) == expected_output

# Test case for a single-grouped IPv6 address
def test_valid_case_single_grouped_ipv6():
    addr = '::1'
    expected_output = '::'
    assert to_ipv6_network(addr) == expected_output
