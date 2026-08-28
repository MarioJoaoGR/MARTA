
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_with_message():
    with pytest.raises(ValueError):
        raise ValueError("The provided pattern does not match the required criteria.")

