
import re
from string_utils.validation import is_ip_v6

# Regular expression for validating an IPv6 address
IP_V6_RE = re.compile(
    r'^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|'
    r'([0-9a-fA-F]{1,4}:){1,7}:|'
    r'([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|'
    r'([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|'
    r'([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|'
    r'([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|'
    r'([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|'
    r'[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|'
    r':((:[0-9a-fA-F]{1,4}){1,7}|:)|'
    r'fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|
    r'::(ffff(:0{1,4}){0,1}:){0,1}'
    r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}'
    r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|'
    r'([0-9a-fA-F]{1,4}:){1,4}:'
    r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}'
    r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'
)

def test_valid_ipv6_address_2001_db8_85a3():
    address = '2001:db8:85a3::8a2e:370:7334'
    assert is_ip_v6(address) == True

def test_valid_ipv6_address_double_colons_only():
    address = '::'
    assert is_ip_v6(address) == True

def test_invalid_ipv6_address_multiple_shorthands():
    address = '2001:db8:85a3::ff00:1::1'
    assert is_ip_v6(address) == False

def test_valid_ipv6_address_full_notation():
    address = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    assert is_ip_v6(address) == True

def test_invalid_ipv6_address_with_question_mark():
    address = '2001:db8:85a3:0000:0000:8a2e:370:?'
    assert is_ip_v6(address) == False

def test_invalid_ipv4_address():
    address = '192.168.1.1'
    assert is_ip_v6(address) == False

def test_empty_string():
    address = ''
    assert is_ip_v6(address) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: unterminated string literal (detected at line 16) (line 16, col 5)
    r'fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|
"""