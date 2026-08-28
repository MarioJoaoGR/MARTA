
import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

# Test initialization of Maybe with a non-empty value (Some)
def test_maybe_with_value():
    maybe = Maybe(42, False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test initialization of Maybe that is "Nothing"
def test_maybe_nothing():
    maybe = Maybe(None, True)
    assert maybe.is_nothing
    with pytest.raises(AttributeError):
        print(maybe.value)

# Test conversion from Maybe to Try when Maybe has a value (Some)
def test_maybe_to_try_with_value():
    maybe = Maybe(42, False)
    try_instance = maybe.to_try()
    assert isinstance(try_instance, Try)
    assert try_instance.is_success
    assert try_instance.value == 42

# Test conversion from Maybe to Try when Maybe is "Nothing"
def test_maybe_to_try_nothing():
    maybe = Maybe(None, True)
    try_instance = maybe.to_try()
    assert isinstance(try_instance, Try)
    assert not try_instance.is_success
    assert try_instance.value is None

# Test initialization of Try with a value (successful Try)
def test_init_try_with_value():
    success = Try(42, True)
    assert success.is_success
    assert success.value == 42

# Test initialization of Try without a value (failed Try)
def test_init_try_without_value():
    failure = Try("error", False)
    assert not failure.is_success