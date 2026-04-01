
import pytest
from string_utils.validation import is_ip_v6, IP_V6_RE

def test_invalid_ipv6():
    # Test cases for invalid IPv6 addresses
    assert not is_ip_v6('')  # Empty string should return False
    assert not is_ip_v6('     ')  # String of spaces should return False
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?')  # Invalid character "?" should return False
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334extra')  # Extra characters after valid IPv6 should return False
