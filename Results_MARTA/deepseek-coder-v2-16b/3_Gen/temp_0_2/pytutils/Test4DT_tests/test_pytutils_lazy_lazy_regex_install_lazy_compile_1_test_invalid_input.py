
import pytest
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile
import re

def test_invalid_input():
    with pytest.raises(TypeError):
        # Attempt to compile a non-string input, which should raise a TypeError
        re.compile(42)
