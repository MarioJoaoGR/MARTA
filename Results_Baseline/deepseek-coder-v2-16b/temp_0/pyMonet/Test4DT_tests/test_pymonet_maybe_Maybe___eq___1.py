
import pytest
from pymonet.maybe import Maybe

# Test equality with another Maybe instance with the same value
def test_eq_with_same_value():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=42, is_nothing=False)
    assert maybe1 == maybe2

# Test equality with another Maybe instance with different value
def test_eq_with_different_value():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=99, is_nothing=False)
    assert not (maybe1 == maybe2)

# Test equality with a non-Maybe instance
def test_eq_with_non_maybe():
    maybe = Maybe(value=42, is_nothing=False)
    other = object()
    assert not (maybe == other)

# Test equality with an empty Maybe instance
def test_eq_with_empty_maybe():
    maybe1 = Maybe(value=None, is_nothing=True)
    maybe2 = Maybe(value=None, is_nothing=True)
    assert maybe1 == maybe2

# Test inequality with a non-empty Maybe instance
def test_neq_with_non_empty_maybe():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=None, is_nothing=True)
    assert not (maybe1 == maybe2)

# Test inequality with a different type of Maybe instance
def test_neq_with_different_type():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=None, is_nothing=True)
    assert not (maybe1 == maybe2)
