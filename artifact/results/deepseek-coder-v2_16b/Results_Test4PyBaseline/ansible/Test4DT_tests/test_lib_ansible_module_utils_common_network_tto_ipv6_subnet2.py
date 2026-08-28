
import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

# Test case for handling IPv6 addresses with more than four groupings
def test_to_ipv6_subnet_more_than_four():
    assert to_ipv6_subnet('2001:db8:1:2:3:4:5:6') == '2001:db8:1:2::'
    assert to_ipv6_subnet('3ffe:1900:1:2:3:4:5:6') == '3ffe:1900:1:2::'

# Test case for handling IPv6 addresses with fewer than four groupings
def test_to_ipv6_subnet_fewer_than_four():
    assert to_ipv6_subnet('2001:db8::') == '2001:db8::'
    assert to_ipv6_subnet('3ffe:1900:1::') == '3ffe:1900:1::'

# Test case for handling IPv6 addresses with omitted zeros
def test_to_ipv6_subnet_omitted_zeros():
    assert to_ipv6_subnet('2001:db8::1') == '2001:db8::'
    assert to_ipv6_subnet('3ffe:1900:1::1') == '3ffe:1900:1::'
    assert to_ipv6_subnet('::1') == '::'

# Test case for handling IPv6 addresses with mixed groupings
def test_to_ipv6_subnet_mixed_groupings():
    assert to_ipv6_subnet('2001:db8:1:2:3::1') == '2001:db8:1:2::'
    assert to_ipv6_subnet('3ffe:1900:1:2:3:4:5::1') == '3ffe:1900:1:2::'

# Test case for ensuring the output ends with '::' if necessary
def test_to_ipv6_subnet_ensure_double_colon():
    assert to_ipv6_subnet('2001:db8::') == '2001:db8::'
    assert to_ipv6_subnet('3ffe:1900:1::') == '3ffe:1900:1::'
    assert to_ipv6_subnet('::1') == '::'
