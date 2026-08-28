
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern


def test_invalid_pattern_empty_message():
    msg = ""
    with pytest.raises(ValueError):
        raise InvalidPattern(msg)
