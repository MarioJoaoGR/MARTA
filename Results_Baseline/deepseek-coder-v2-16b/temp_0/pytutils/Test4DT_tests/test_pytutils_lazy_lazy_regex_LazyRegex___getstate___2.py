
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

# Test initialization with default arguments
def test_init_default():
    lazy_regex = LazyRegex()
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ()
    assert lazy_regex._regex_kwargs == {}

# Test initialization with specific pattern and flags
def test_init_with_pattern_and_flags():
    lazy_regex = LazyRegex(r'\d+', re.IGNORECASE)
    assert lazy_regex._real_regex is None