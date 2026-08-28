# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating an empty Maybe
def test_create_empty_maybe():
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.is_nothing
    with pytest.raises(AttributeError):
        print(nothing.value)

# Test checking if the Maybe contains a value and retrieving it safely
def test_check_and_retrieve_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating a Maybe with a non-empty value using the helper method
def test_create_maybe_with_non_empty_value():
    maybe_some = Maybe.just(10)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 10

# Test creating an empty Maybe using the helper method
def test_create_empty_maybe_using_helper_method():
    maybe_nothing = Maybe.nothing()
    assert maybe_nothing.is_nothing

# Test filtering the value contained in the Maybe monad based on a provided predicate function
def is_even(x):
    return x % 2 == 0

def test_filter_value():
    maybe_some = Maybe.just(10)
    filtered_maybe = maybe_some.filter(is_even)
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 10

# Test filtering the value contained in the Maybe monad based on a provided predicate function with an odd number
def test_filter_odd_number():
    maybe_some = Maybe.just(9)
    filtered_maybe = maybe_some.filter(is_even)
    assert filtered_maybe.is_nothing

# Test filtering the value contained in the Maybe monad based on a provided predicate function with an even number
def test_filter_even_number():
    maybe_some = Maybe.just(8)
    filtered_maybe = maybe_some.filter(is_even)
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 8
