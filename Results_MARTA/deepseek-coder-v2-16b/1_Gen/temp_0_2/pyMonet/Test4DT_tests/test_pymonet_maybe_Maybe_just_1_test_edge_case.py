
import pytest
from pymonet.maybe import Maybe

def test_just():
    # Test creating a not-empty Maybe object
    maybe = Maybe.just(42)
    assert maybe.is_nothing is False
    assert maybe.value == 42

    # Test creating a not-empty Maybe object with None value
    maybe_none = Maybe.just(None)
    assert maybe_none.is_nothing is False
    assert maybe_none.value is None

    # Test creating an empty Maybe object
    nothing = Maybe(None, True)
    assert nothing.is_nothing is True
    with pytest.raises(AttributeError):
        print(nothing.value)  # This should raise an AttributeError because it's not supposed to be accessible when is_nothing is True
