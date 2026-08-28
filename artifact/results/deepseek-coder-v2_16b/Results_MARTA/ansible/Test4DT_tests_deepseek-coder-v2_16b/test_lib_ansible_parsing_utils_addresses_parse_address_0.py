
import pytest
from ansible.parsing.utils.addresses import parse_address
from ansible.errors import AnsibleError, AnsibleParserError

# Test cases for valid IPv4 address without port
def test_valid_case_1():
    result = parse_address("192.168.1.1")
    assert result == ('192.168.1.1', None)

# Test cases for valid IPv6 address without port
def test_valid_case_2():
    result = parse_address("::1")
    assert result == ('::1', None)

# Test cases for valid hostname with alphanumeric ranges

# Test cases for valid IPv4 address with port
def test_valid_case_4():
    result = parse_address("192.168.1.1:8080")
    assert result == ('192.168.1.1', 8080)

# Test cases for valid IPv6 address with port in brackets

# Test cases for valid hostname with port
def test_valid_case_6():
    result = parse_address("example.com:8080")
    assert result == ('example.com', 8080)

# Test cases for error case when allowing ranges but not specified
def test_error_case_1():
    with pytest.raises(AnsibleError):
        parse_address("example[1:3].com")

# Test cases for valid hostname with port and allowing ranges

# Test cases for error case when parsing `None`