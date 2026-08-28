
import pytest
from string_utils.validation import is_ip

def test_valid_ipv4():
    assert is_ip('255.200.100.75') == True

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True

def test_invalid_ipv4_too_short():
    assert is_ip('1.2.3') == False

def test_invalid_ipv6_too_long():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334:1234') == False

def test_invalid_ip_format():
    assert is_ip('invalid-ip-address') == False

def test_empty_string():
    assert is_ip('') == False

def test_none_input():
    assert is_ip(None) == False

def test_whitespace_only():
    assert is_ip('   ') == False
