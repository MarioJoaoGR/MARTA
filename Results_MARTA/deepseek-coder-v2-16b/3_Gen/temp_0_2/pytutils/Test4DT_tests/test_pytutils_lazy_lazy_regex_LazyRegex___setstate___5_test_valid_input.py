
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_input():
    lazy_regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    assert lazy_regex._real_regex is None
    assert lazy_regex._regex_args == ("pattern",)
    assert lazy_regex._regex_kwargs == {"flags": 0}
