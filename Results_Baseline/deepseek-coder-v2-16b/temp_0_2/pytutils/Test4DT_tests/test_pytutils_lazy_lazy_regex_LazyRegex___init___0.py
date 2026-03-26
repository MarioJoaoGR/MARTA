
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

# Test initialization with default arguments
def test_default_initialization():
    lazy_regex = LazyRegex()
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ()
    assert lazy_regex._regex_kwargs == {}

# Test initialization with provided args and kwargs
def test_initialization_with_args_and_kwargs():
    lazy_regex = LazyRegex(args=("pattern", re.IGNORECASE))
    assert lazy_regex._real_regex is None