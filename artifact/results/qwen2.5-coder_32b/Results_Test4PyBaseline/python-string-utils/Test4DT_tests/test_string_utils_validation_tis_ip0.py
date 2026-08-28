
import pytest
from string_utils.validation import is_ip

def test_valid_ipv4_addresses():
    assert is_ip('255.200.100.75'), "Valid IPv4 address should return True"
    assert is_ip('192.168.1.1'), "Valid IPv4 address should return True"
    assert is_ip('0.0.0.0'), "Valid IPv4 address should return True"
    assert is_ip('255.255.255.255'), "Valid IPv4 address should return True"

def test_invalid_ipv4_addresses():
    assert not is_ip('1.2.3'), "Invalid IPv4 address should return False"
    assert not is_ip('999.999.999.999'), "Out of range IPv4 address should return False"
    assert not is_ip('256.256.256.256'), "Out of range IPv4 address should return False"