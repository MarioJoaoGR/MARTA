
import pytest
from sanic import Sanic
from sanic.response import json

# Create a simple Sanic app for testing
app = Sanic("TestApp")

@app.route("/test")
async def test_endpoint(request):
    return json({"message": "Hello, world!"})

# Define the fwd_normalize_address function to be tested
def fwd_normalize_address(addr: str) -> str:
    """Normalize address fields of proxy headers."""
    if addr == "unknown":
        raise ValueError()  # omit unknown value identifiers
    if addr.startswith("_"):
        return addr  # do not lower-case obfuscated strings
    if _ipv6_re.fullmatch(addr):
        addr = f"[{addr}]"  # bracket IPv6
    return addr.lower()

# Test cases for fwd_normalize_address function


def test_fwd_normalize_address_obfuscated():
    assert fwd_normalize_address("_hiddenvalue") == "_hiddenvalue"

def test_fwd_normalize_address_unknown():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")