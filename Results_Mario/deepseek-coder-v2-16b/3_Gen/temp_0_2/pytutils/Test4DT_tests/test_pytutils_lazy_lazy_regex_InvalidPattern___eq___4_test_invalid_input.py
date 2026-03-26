
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_input():
    # Test when other is not an instance of InvalidPattern
    invalid_other = "not an instance"
    assert InvalidPattern("Invalid pattern") != invalid_other

    # Test when both instances have the same message
    ip1 = InvalidPattern("Invalid pattern")
    ip2 = InvalidPattern("Invalid pattern")
    assert ip1 == ip2

    # Test when messages are different
    ip3 = InvalidPattern("Different invalid pattern")
    assert InvalidPattern("Invalid pattern") != ip3
