
import pytest

def test_valid_inputs():
    def evalString(s):
        return eval(s)
    
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, f"ASCII {i} does not match its representation: {repr(c)} -> {e}"

def test_edge_cases():
    def evalString(s):
        return eval(s)
    
    # Test with an empty range
    for i in range(0):
        c = chr(i) if i < 256 else None
        s = repr(c)
        e = evalString(s)
        assert e == c, f"ASCII {i} does not match its representation: {repr(c)} -> {e}"

def test_invalid_inputs():
    def evalString(s):
        return eval(s)
    
    # Test with an invalid ASCII code (256 is beyond the valid range for chr)
    i = 256
    c = chr(i)
    s = repr(c)
    e = evalString(s)
    assert e == c, f"ASCII {i} does not match its representation: {repr(c)} -> {e}"
