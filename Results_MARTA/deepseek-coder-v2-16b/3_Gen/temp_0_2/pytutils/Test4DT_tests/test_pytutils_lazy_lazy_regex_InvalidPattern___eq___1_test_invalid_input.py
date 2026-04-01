
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern():
    # Test case for creating an InvalidPattern instance with a specific message
    msg = "The provided pattern does not match any expected format."
    try:
        raise InvalidPattern(msg)
    except InvalidPattern as e:
        assert e.msg == msg

def test_invalid_pattern_equality():
    # Test case for checking equality of two InvalidPattern instances with the same message
    msg1 = "The provided pattern does not match any expected format."
    msg2 = "Another invalid pattern message."
    
    ip1 = InvalidPattern(msg1)
    ip2 = InvalidPattern(msg1)
    ip3 = InvalidPattern(msg2)
    
    assert ip1 == ip2  # Instances with the same message should be equal
    assert not (ip1 == ip3)  # Instances with different messages should not be equal
