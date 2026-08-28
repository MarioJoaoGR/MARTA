
import pytest
from string_utils.validation import is_ip_v4

def test_valid_ipv4_addresses():
    assert is_ip_v4('255.200.100.75'), "Test case 255.200.100.75 failed"
    assert is_ip_v4('192.168.1.1'), "Test case 192.168.1.1 failed"
    assert is_ip_v4('0.0.0.0'), "Test case 0.0.0.0 failed"
    assert is_ip_v4('255.255.255.255'), "Test case 255.255.255.255 failed"

def test_invalid_ipv4_addresses():
    assert not is_ip_v4('nope'), "Test case 'nope' failed"
    assert not is_ip_v4('255.200.100.999'), "Test case 255.200.100.999 failed"
    assert not is_ip_v4('1.2.3'), "Test case 1.2.3 failed"
    assert not is_ip_v4('256.256.256.256'), "Test case 256.256.256.256 failed"

def test_edge_cases():
    assert is_ip_v4('0.0.0.0'), "Edge case 0.0.0.0 failed"
    assert is_ip_v4('255.255.255.255'), "Edge case 255.255.255.255 failed"

def test_empty_and_whitespace_strings():
    assert not is_ip_v4(''), "Test case empty string failed"
    assert not is_ip_v4('   '), "Test case whitespace string failed"
    assert not is_ip_v4('\t\n'), "Test case newline and tab string failed"

def test_non_string_input():
    assert not is_ip_v4(None), "Non-string input None should return False"
    assert not is_ip_v4(12345), "Non-string input integer should return False"
    assert not is_ip_v4(['192.168.1.1']), "Non-string input list should return False"
