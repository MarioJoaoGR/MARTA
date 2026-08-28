
import pytest
from unittest.mock import patch
from string_utils.validation import is_ip_v6, IP_V6_RE

# Test valid IPv6 address
def test_valid_ipv6():
    with patch('string_utils.validation.IP_V6_RE', return_value=True):
        assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

# Test invalid IPv6 address due to an invalid character ('?')

# Test invalid IPv6 address due to being empty after stripping whitespace
def test_invalid_empty():
    with patch('string_utils.validation.IP_V6_RE', return_value=False):
        assert is_ip_v6(' ') == False