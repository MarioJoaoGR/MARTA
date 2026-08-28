
import re
from ansible.module_utils.common.network import is_mac

def test_is_mac_valid_hyphen():
    assert is_mac("12-34-56-78-9A-BC") == True

def test_is_mac_valid_colon():
    assert is_mac("12:34:56:78:9A:BC") == True

def test_is_mac_invalid_format():
    assert is_mac("1234.5678.9ABC") == False

def test_is_mac_invalid_character():
    assert is_mac("12-34-56-78-9A-CG") == False

# Additional tests to cover uncovered lines 160-161

def test_is_mac_valid_mixed_case():
    # Test with a valid MAC address in mixed case (should be treated as lower case)
    assert is_mac("12:34:56:78:9A:bc") == True

def test_is_mac_invalid_length():
    # Test with an invalid length (should be False)
    assert is_mac("12-34-56-78-9A") == False

def test_is_mac_empty_string():
    # Test with an empty string (should be False)
    assert is_mac("") == False
