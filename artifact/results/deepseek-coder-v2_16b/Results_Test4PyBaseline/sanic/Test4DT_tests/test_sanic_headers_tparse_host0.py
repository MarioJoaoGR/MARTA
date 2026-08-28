
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

def test_invalid_host():
    result = parse_host('invalid-host')