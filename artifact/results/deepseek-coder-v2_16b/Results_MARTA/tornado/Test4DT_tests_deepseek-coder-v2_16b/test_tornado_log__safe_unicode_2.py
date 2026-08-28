
import pytest
from typing import Any

def _safe_unicode(s: Any) -> str:
    try:
        return s.decode('utf-8') if isinstance(s, bytes) else str(s)
    except (UnicodeDecodeError, AttributeError):
        return repr(s)

# Test for basic functionality of _safe_unicode function
def test__safe_unicode_basic():
    # Test with a Unicode string
    assert _safe_unicode("Hello, World!") == "Hello, World!"
    
    # Test with a bytes object that can be decoded
    assert _safe_unicode(b"Hello, World!") == "Hello, World!"
    
    # Test with a bytes object that cannot be decoded
    assert _safe_unicode(b"\x80\x81\x82") == repr(b"\x80\x81\x82")
    
    # Test with an integer, which will be converted using repr
    assert _safe_unicode(42) == "42"
