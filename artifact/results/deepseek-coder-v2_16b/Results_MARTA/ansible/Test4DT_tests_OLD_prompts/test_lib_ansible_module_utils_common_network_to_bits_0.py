
import pytest
from ansible.module_utils.common.network import to_bits

def test_to_bits_basic():
    # Test with a basic netmask in dotted decimal notation
    assert to_bits('255.255.255.0') == '11111111111111111111111100000000'
    
    # Test with another netmask in dotted decimal notation
    assert to_bits('192.168.1.1') == '11000000101010000000000100000001'
