
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_edge_case_none():
    with pytest.raises(TypeError):
        lazy_regex = LazyRegex()
        getattr(lazy_regex, 'non_existent_attribute')
