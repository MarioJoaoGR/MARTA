
import pytest
from ansible.parsing.utils.addresses import parse_address
from ansible.errors import AnsibleError, AnsibleParserError

# Test cases for valid IPv4 addresses
def test_parse_address_valid_ipv4():
    assert parse_address("192.168.1.1") == ('192.168.1.1', None)

# Test cases for valid IPv6 addresses
def test_parse_address_valid_ipv6():
    assert parse_address("::1") == ('::1', None)

# Test cases for valid hostnames with ports
def test_parse_address_valid_hostname_with_port():
    assert parse_address("example.com:8080") == ('example.com', 8080)

# Test cases for valid IPv4 addresses with ports
def test_parse_address_valid_ipv4_with_port():
    assert parse_address("192.168.1.1:8080") == ('192.168.1.1', 8080)

# Test cases for valid IPv6 addresses with ports
def test_parse_address_valid_ipv6_with_port():
    assert parse_address("[::1]:8080") == ('::1', 8080)

# Test cases for hostnames with ranges (if allow_ranges is True)
def test_parse_address_hostname_with_ranges_allowed():
    assert parse_address("example[1:3].com", allow_ranges=True) == ('example[1:3].com', None)

# Test cases for invalid addresses
def test_parse_address_invalid_address():
    with pytest.raises(AnsibleError):
        parse_address("invalid-address")

# Test cases for handling ranges in host part when allow_ranges is False
def test_parse_address_range_in_host_not_allowed():
    with pytest.raises(AnsibleParserError):
        parse_address("[::1]:8080")

if __name__ == "__main__":
    pytest.main()
