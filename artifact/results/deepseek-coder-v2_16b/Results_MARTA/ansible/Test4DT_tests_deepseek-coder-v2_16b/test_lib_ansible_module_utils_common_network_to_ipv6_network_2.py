
import pytest
from ansible.module_utils.common.network import to_ipv6_network

def test_to_ipv6_network_full():
    assert to_ipv6_network('2001:db8::1') == '2001:db8::'


def test_to_ipv6_network_single_group():
    assert to_ipv6_network('::1') == '::'