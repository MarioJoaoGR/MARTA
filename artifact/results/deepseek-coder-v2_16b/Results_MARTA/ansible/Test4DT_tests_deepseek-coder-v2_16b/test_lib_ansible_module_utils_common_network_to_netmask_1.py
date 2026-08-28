
import pytest
from ansible.module_utils.common.network import to_netmask

def is_masklen(val):
    try:
        masklen = int(val)
        if 0 <= masklen <= 32:
            return True
    except ValueError:
        pass
    return False

# Helper function to convert bits to dotted decimal notation
from struct import pack
from socket import inet_ntoa

def test_valid_case_24():
    val = '24'
    assert to_netmask(val) == '255.255.255.0'

def test_valid_case_30():
    val = '30'
    assert to_netmask(val) == '255.255.255.252'

def test_invalid_case_33():
    val = '33'
    with pytest.raises(ValueError):
        to_netmask(val)
