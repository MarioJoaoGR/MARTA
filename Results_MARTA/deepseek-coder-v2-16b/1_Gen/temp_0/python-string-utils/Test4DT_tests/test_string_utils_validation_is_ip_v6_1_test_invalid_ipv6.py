
import pytest
from string_utils.validation import is_ip_v6

def test_invalid_ipv6():
    # Test cases for invalid IPv6 addresses
    assert not is_ip_v6(' ')  # Empty or whitespace-only string should return False
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?')  # Invalid character '?'
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334:7334')  # Too many segments
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370')  # Missing segment
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370::7334')  # Double colon
