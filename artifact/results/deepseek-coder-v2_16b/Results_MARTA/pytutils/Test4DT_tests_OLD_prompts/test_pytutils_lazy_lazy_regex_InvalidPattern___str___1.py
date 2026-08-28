
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern


def test_invalid_pattern_with_default_message():
    with pytest.raises(TypeError):
        InvalidPattern()