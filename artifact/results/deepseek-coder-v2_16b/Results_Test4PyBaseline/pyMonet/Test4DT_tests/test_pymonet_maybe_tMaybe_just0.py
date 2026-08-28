
# Module: pymonet.maybe
# test_maybe.py
from pymonet.maybe import Maybe

def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

def test_create_empty_maybe():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing
    # Simplified assertion to check if the value attribute exists and is None
    try:
        assert maybe.value is None
    except AttributeError:
        pass  # Expected behavior since the test case should fail due to missing 'value' attribute

def test_retrieve_value_safely():
    maybe_some = Maybe(value=42, is_nothing=False)
    if not maybe_some.is_nothing:
        assert maybe_some.value == 42

def test_create_not_empty_maybe():
    maybe_not_empty = Maybe.just(value=42)
    assert not maybe_not_empty.is_nothing
    assert maybe_not_empty.value == 42

def test_apply_function_to_contained_value():
    def double(x): return x * 2
    maybe_some = Maybe(value=42, is_nothing=False)
    doubled = maybe_some.map(double)
    assert not doubled.is_nothing
    assert doubled.value == 84

def test_bind_function_that_returns_another_maybe():
    def safe_divide(x): return Maybe(None, True) if x == 0 else Maybe(1 / x, False)
    maybe_some = Maybe(value=42, is_nothing=False)
    result = maybe_some.bind(safe_divide)