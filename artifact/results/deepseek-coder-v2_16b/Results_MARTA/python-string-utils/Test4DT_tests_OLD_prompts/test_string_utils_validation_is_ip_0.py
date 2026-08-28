
import pytest
from string_utils.validation import is_ip

# Test valid IPv4 address
def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True

# Test valid IPv6 address
def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

# Test invalid IP address (not an IPv6)
def test_invalid_ip():
    assert is_ip('1.2.3') == False
