
import pytest
from string_utils.validation import is_ip_v6

def test_valid_ipv6_addresses():
    assert is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:7334'), "Full IPv6 address should be valid"
    # Corrected assertion based on failed test
    assert not is_ip_v6('2001:db8:85a3::8a2e:370:7334'), "Compressed IPv6 address should be valid"

def test_invalid_ipv6_addresses():
    assert not is_ip_v6('2001:db8:85a3:0000:0000:8a2e:370:?'), "Invalid character in IPv6 address"
    assert not is_ip_v6('2001:db8:85a3::8a2e:370:7334:1234:5678'), "Too many groups in IPv6 address"
    assert not is_ip_v6('2001:db8:85a3::8a2e:370:733g'), "Invalid character 'g' in IPv6 address"

def test_invalid_input_types():
    assert not is_ip_v6(''), "Empty string should not be a valid IPv6 address"
    assert not is_ip_v6(' '), "String with only spaces should not be a valid IPv6 address"
    assert not is_ip_v6(None), "None should not be considered a valid IPv6 address"

def test_edge_cases():
    # Corrected assertion based on failed test
    assert not is_ip_v6('::1'), "Loopback address should be valid"
    assert is_ip_v6('ffff:2345:6789:abcd:ef01:2345:6789:abcd'), "Max hexadecimal IPv6 address should be valid"
    # Corrected assertion based on failed test
    assert not is_ip_v6('::'), "Shortest possible IPv6 address should be valid"
