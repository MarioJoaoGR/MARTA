
import pytest
from sanic import Sanic
from unittest.mock import patch

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


def test_obfuscated_string():
    normalized_addr = fwd_normalize_address("_hiddenvalue")
    assert normalized_addr == "_hiddenvalue"
