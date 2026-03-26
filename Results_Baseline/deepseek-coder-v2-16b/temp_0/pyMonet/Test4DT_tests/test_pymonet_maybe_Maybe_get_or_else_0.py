
# Module: pymonet.maybe
# test_maybe.py
from pymonet.maybe import Maybe
import pytest

@pytest.fixture
def maybe_with_value():
    return Maybe(value=42, is_nothing=False)

@pytest.fixture
def empty_maybe():
    return Maybe(value=None, is_nothing=True)

def test_init_with_value(maybe_with_value):
    assert maybe_with_value.is_nothing == False
    assert maybe_with_value.value == 42

def test_init_empty():
    empty = Maybe(value=None, is_nothing=True)
    assert empty.is_nothing == True