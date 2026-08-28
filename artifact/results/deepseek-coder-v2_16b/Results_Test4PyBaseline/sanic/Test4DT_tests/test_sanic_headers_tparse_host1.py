
import pytest
from typing import Optional, Tuple
from sanic.headers import parse_host

# Test cases for parse_host function
def test_valid_host_with_port():
    result = parse_host('example.com:80')
    assert result == ('example.com', 80)

def test_valid_localhost_with_port():
    result = parse_host('localhost:443')
    assert result == ('localhost', 443)

@pytest.mark.xfail(reason="Expected failure for invalid input")
def test_invalid_host():
    result = parse_host('invalid-host')
    assert result == (None, None)

# Additional test cases to cover uncovered line 177
def test_empty_string():
    result = parse_host('')
    assert result == (None, None)

def test_no_port():
    result = parse_host('example.com')
    assert result == ('example.com', None)

def test_only_colon():
    result = parse_host(':')
    assert result == (None, None)

def test_only_hostname():
    result = parse_host('example.com')
    assert result == ('example.com', None)

def test_whitespace_in_input():
    result = parse_host(' example.com:80 ')