
import pytest
from string_utils.validation import is_ip  # Assuming this module contains the is_ip function

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
