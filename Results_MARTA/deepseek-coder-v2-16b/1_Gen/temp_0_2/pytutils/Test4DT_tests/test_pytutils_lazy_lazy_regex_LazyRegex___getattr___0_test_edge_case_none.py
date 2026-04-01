
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_edge_case_none():
    lazy_regex = LazyRegex(None, {})
    with pytest.raises(AttributeError):
        # Attempting to access an attribute of the real regex before it is compiled should raise an AttributeError
        getattr(lazy_regex._real_regex, 'findall')
