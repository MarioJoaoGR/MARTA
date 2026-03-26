
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

# Test cases for the __init__ method of InvalidPattern class
def test_invalid_pattern_init():
    msg = "Invalid pattern error message"
    err = InvalidPattern(msg)
    assert err.msg == msg

# Test cases for the __eq__ method of InvalidPattern class
def test_invalid_pattern_equal():
    msg1 = "First invalid pattern error message"
    err1 = InvalidPattern(msg1)
    err2 = InvalidPattern(msg1)
    assert err1 == err2

# Test cases for the __eq__ method with different classes
def test_invalid_pattern_not_equal():
    msg = "Invalid pattern error message"
    err1 = InvalidPattern(msg)
    class OtherClass: pass
    err2 = OtherClass()
    assert not (err1 == err2)

# Test cases for the __eq__ method with different instances
def test_invalid_pattern_not_equal_instances():
    msg1 = "First invalid pattern error message"
    msg2 = "Second invalid pattern error message"
    err1 = InvalidPattern(msg1)
    err2 = InvalidPattern(msg2)
    assert not (err1 == err2)

# Test cases for the __str__ method of InvalidPattern class
def test_invalid_pattern_str():
    msg = "Invalid pattern error message"
    err = InvalidPattern(msg)
    expected_str = f'Invalid pattern(s) found. {err.msg}'