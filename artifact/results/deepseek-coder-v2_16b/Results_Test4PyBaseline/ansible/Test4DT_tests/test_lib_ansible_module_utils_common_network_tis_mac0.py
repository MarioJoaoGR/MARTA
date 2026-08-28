# Module: ansible.module_utils.common.network
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
