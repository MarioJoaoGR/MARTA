
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_none_input():
    # Test when msg is None
    try:
        raise InvalidPattern(None)
    except InvalidPattern as e:
        assert e.msg is None
