
import pytest
from string_utils.validation import is_ip_v4

def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.255.255.255') == True

def test_invalid_ipv4():
    assert not is_ip_v4('nope')
    assert not is_ip_v4('255.200.100.999')
    assert not is_ip_v4('256.200.100.75')
    assert not is_ip_v4('255.200.100')
    assert not is_ip_v4('192.168.1')
