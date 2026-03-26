
import re
from pytutils.lazy.lazy_regex import lazy_compile, LazyRegex

def test_none_input():
    # Test that passing None as a positional argument raises a TypeError
    try:
        lazy_compile(None)
    except TypeError as e:
        assert str(e) == "Expected at least one argument (the regex pattern), got 1"
    
    # Test that passing None as a keyword argument raises a TypeError
    try:
        lazy_compile(pattern=None)
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'pattern'"
