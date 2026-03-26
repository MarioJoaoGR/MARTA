# Module: string_utils.validation
import pytest
from string_utils.validation import is_ip_v6

# Test cases for the is_ip_v6 function
def test_valid_ipv6():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_invalid_ipv6_due_to_invalid_character():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?') == False

def test_invalid_ipv6_due_to_empty_string():
    assert is_ip_v6('') == False

def test_invalid_ipv6_due_to_string_consisting_only_of_spaces():
    assert is_ip_v6(' ') == False
