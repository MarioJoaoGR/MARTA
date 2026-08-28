
import pytest
from sanic import Sanic
from sanic.headers import fwd_normalize_address

def test_fwd_normalize_address_normal():
    assert fwd_normalize_address("example.com") == "example.com"

def test_fwd_normalize_address_ipv6():
    assert fwd_normalize_address("[2001:db8::1]") == "[2001:db8::1]"

def test_fwd_normalize_address_obfuscated():
    assert fwd_normalize_address("_hiddenvalue") == "_hiddenvalue"

def test_fwd_normalize_address_unknown():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")
