# Module: pymonet.maybe
# Import the Maybe class from the pymonet module
from pymonet.maybe import Maybe

def test_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

def test_maybe_with_none():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing
    try:
        _ = maybe.value
        assert False, "Expected AttributeError"
    except AttributeError:
        pass

def test_maybe_equality():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=42, is_nothing=False)
    maybe3 = Maybe(value="hello", is_nothing=True)
    
    assert maybe1 == maybe2
    assert not (maybe1 == maybe3)
