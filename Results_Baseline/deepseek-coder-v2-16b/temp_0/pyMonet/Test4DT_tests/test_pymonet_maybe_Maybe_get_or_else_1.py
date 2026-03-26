
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

# Test initialization with a value
def test_init_with_value(maybe_with_value):
    assert maybe_with_value.is_nothing == False
    assert maybe_with_value.value == 42

# Test initialization when Maybe is empty
def test_init_empty():
    empty = Maybe(value=None, is_nothing=True)
    assert empty.is_nothing == True

# Test get_or_else method with a value in Maybe
def test_get_or_else_with_value(maybe_with_value):
    default_value = "default"
    result = maybe_with_value.get_or_else(default_value)
    assert result == 42

# Test get_or_else method with an empty Maybe
def test_get_or_else_empty(empty_maybe):
    default_value = "default"
    result = empty_maybe.get_or_else(default_value)
    assert result == default_value

# Test get_or_else method with a non-default value in Maybe
def test_get_or_else_non_default(maybe_with_value):
    default_value = "default"
    result = maybe_with_value.get_or_else(default_value)
    assert result == 42

# Test get_or_else method with a different non-default value in Maybe
def test_get_or_else_different_non_default(maybe_with_value):
    default_value = "alternative"
    result = maybe_with_value.get_or_else(default_value)
    assert result == 42
