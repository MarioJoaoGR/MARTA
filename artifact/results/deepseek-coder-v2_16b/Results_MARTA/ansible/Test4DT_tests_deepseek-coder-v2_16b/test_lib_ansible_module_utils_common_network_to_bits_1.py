
import pytest
from ansible.module_utils.common.network import to_bits

def test_to_bits_valid_input():
    """ Test handling of a valid input (string representing a netmask) """
    assert to_bits('255.255.255.0') == '11111111111111111111111100000000'
    assert to_bits('192.168.1.1') == '11000000101010000000000100000001'

