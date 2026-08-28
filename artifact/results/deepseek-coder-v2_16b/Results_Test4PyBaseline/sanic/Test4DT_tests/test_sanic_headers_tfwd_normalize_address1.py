
# Module: sanic.headers
# test_sanic_headers.py
from sanic.headers import fwd_normalize_address
import pytest

def test_fwd_normalize_address_ipv4():
    assert fwd_normalize_address("192.168.1.1") == "192.168.1.1"

def test_fwd_normalize_address_domain():
    assert fwd_normalize_address("example.com") == "example.com"

def test_fwd_normalize_address_obfuscated():
    assert fwd_normalize_address("_hiddenValue") == "_hiddenValue"

# New test case to cover the normalization of IPv6 addresses
def test_fwd_normalize_address_ipv6():
    assert fwd_normalize_address("2001:db8::1") == "[2001:db8::1]"

# Test case for handling unknown values, which should raise a ValueError
def test_fwd_normalize_address_unknown():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")
