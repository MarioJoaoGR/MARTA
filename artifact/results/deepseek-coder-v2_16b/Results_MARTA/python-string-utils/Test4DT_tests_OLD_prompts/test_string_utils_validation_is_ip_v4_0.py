
import pytest
from unittest.mock import patch
from string_utils.validation import is_ip_v4, SHALLOW_IP_V4_RE, is_full_string

# Test for valid IPv4 address
def test_valid_ip():
    assert is_ip_v4('255.200.100.75') == True

# Test for input with invalid characters
def test_invalid_chars():
    assert is_ip_v4('nope') == False

# Test for None input
def test_none_input():
    assert is_ip_v4(None) == False
