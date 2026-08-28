
import pytest
from ansible.module_utils.common.network import to_masklen, is_netmask

# Test cases for valid inputs
def test_valid_dot_decimal():
    assert to_masklen("255.255.255.0") == 24
    # Additional valid netmask tests
    assert to_masklen("255.255.255.192") == 26
    assert to_masklen("255.255.255.224") == 27
    assert to_masklen("255.255.255.240") == 28
    assert to_masklen("255.255.255.248") == 29