
import pytest
from ansible.module_utils.common.network import to_ipv6_network

# Test cases for the function `to_ipv6_network`
def test_to_ipv6_network():
    # Test case 1: Standard IPv6 address with all eight groupings present
    assert to_ipv6_network('2001:db8::1') == '2001:db8::'
    
    # Test case 2: An IPv6 address with fewer than three groupings, which should be supplemented by '::'