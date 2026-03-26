
import pytest
from string_utils.validation import is_ip

# Test cases for valid IPv4 addresses
def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True
    assert is_ip('0.0.0.0') == True
    assert is_ip('192.168.1.1') == True

# Test cases for valid IPv6 addresses
def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True