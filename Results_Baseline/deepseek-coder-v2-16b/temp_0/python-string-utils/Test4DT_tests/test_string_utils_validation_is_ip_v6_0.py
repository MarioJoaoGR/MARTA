# Module: string_utils.validation
import pytest
from string_utils.validation import is_ip_v6

# Test cases for the is_ip_v6 function
def test_valid_ipv6():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_invalid_ipv6_character():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') == False

def test_whitespace_string():
    assert is_ip_v6(' ') == False

def test_valid_ipv6_mixed_case():
    assert is_ip_v6('2001:DB8:85A3:0000:0000:8A2E:370:7334') == True

def test_invalid_trailing_punctuation():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334!') == False
