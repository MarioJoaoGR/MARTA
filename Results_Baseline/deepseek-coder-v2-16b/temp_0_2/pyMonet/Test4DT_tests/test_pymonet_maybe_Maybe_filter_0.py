
# Module: pymonet.maybe
# test_maybe.py
from pymonet.maybe import Maybe
import pytest

@pytest.fixture
def maybe_some():
    return Maybe(value=42, is_nothing=False)

@pytest.fixture
def maybe_none():
    return Maybe(value=None, is_nothing=True)

def test_filter_non_empty_maybe(maybe_some):
    filtered_maybe = maybe_some.filter(lambda x: x > 10)
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 42

def test_filter_empty_maybe(maybe_none):
    filtered_maybe = maybe_none.filter(lambda x: x > 10)
    assert filtered_maybe.is_nothing

def test_filter_with_false_predicate(maybe_some):
    filtered_maybe = maybe_some.filter(lambda x: x > 20)