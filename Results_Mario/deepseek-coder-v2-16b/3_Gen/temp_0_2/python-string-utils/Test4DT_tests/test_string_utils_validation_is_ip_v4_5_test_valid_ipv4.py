
import pytest
from string_utils.validation import is_ip_v4, SHALLOW_IP_V4_RE

def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.255.255.255') == True

def test_invalid_ipv4():
    assert is_ip_v4('nope') == False
    assert is_ip_v4('256.200.100.75') == False  # out of range
    assert is_ip_v4('255.200.100.999') == False  # out of range
    assert is_ip_v4('192.168.1.256') == False  # out of range
    assert is_ip_v4('192.168.0') == False  # not enough segments
    assert is_ip_v4('192.168.0.0.0') == False  # too many segments
    assert is_ip_v4('192.168..1') == False  # invalid segment
