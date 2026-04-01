
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_edge_case_none():
    lazy_regex = LazyRegex()
    with pytest.raises(TypeError):
        # Since the regex is not initialized, accessing any method should raise a TypeError
        getattr(lazy_regex, 'findall')("test")
