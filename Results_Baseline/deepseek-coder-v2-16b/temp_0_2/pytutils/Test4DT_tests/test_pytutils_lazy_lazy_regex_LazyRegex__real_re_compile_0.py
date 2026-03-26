
import pytest
from pytutils.lazy.lazy_regex import LazyRegex, _real_re_compile, re, InvalidPattern

@pytest.fixture
def lazy_regex():
    return LazyRegex(args=("initial_pattern",))

def test_basic_usage(lazy_regex):
    matches = lazy_regex.findall("hello world! hello universe!")
    assert isinstance(matches, list), "Expected findall to return a list"