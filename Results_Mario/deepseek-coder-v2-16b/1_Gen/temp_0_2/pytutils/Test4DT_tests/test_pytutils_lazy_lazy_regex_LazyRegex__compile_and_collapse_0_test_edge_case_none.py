
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_edge_case_none():
    lazy_regex = LazyRegex(None, {})
    assert isinstance(lazy_regex._real_regex, type(None))
