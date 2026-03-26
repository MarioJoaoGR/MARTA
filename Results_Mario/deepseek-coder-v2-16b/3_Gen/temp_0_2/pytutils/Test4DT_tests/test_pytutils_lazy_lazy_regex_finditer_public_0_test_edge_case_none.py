
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

@pytest.fixture(scope="module")
def finditer_public():
    def _finditer_public(pattern, string, flags=0):
        if isinstance(pattern, LazyRegex):
            return pattern.finditer(string)
        else:
            return re.compile(pattern, flags).finditer(string)
    return _finditer_public

def test_edge_case_none(finditer_public):
    # Test edge case where the input string is None
    pattern = r'\d+'
    string = None
    with pytest.raises(TypeError):
        list(finditer_public(pattern, string))
