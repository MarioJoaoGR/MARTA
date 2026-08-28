
import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

def test_to_ipv6_subnet_basic():
    assert to_ipv6_subnet('2001:db8::1') == '2001:db8::'