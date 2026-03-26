
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_setstate():
    lazy_regex = LazyRegex()
    state = {"args": (r"pattern",), "kwargs": {"flags": 0}}
    lazy_regex.__setstate__(state)
    
    assert lazy_regex._regex_args == (r"pattern",)
    assert lazy_regex._regex_kwargs == {"flags": 0}
