
import pytest
from pymonet.maybe import Maybe

# Test initialization of Maybe with a value
def test_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test initialization of Maybe that is "Nothing"
def test_maybe_nothing():
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.is_nothing
    with pytest.raises(AttributeError):
        print(nothing.value)  # This should raise an AttributeError because the value is not set

# Test bind method when Maybe is "Nothing"
def test_bind_when_nothing():
    def mapper(_):
        return Maybe(value="mapped", is_nothing=False)
    
    nothing = Maybe(value=None, is_nothing=True)
    result = nothing.bind(mapper)
    assert result.is_nothing
    with pytest.raises(AttributeError):  # The bind method should not call the mapper when Maybe is "Nothing"
        print(result.value)

# Test bind method when Maybe has a value
def test_bind_when_has_value():
    maybe = Maybe(value=42, is_nothing=False)
    
    def mapper(x):
        return Maybe(value=x * 2, is_nothing=False)
    
    result = maybe.bind(mapper)
    assert not result.is_nothing
    assert result.value == 84  # The bind method should call the mapper with the value of Maybe

# Test static method nothing
def test_static_method_nothing():
    nothing = Maybe.nothing()
    assert nothing.is_nothing