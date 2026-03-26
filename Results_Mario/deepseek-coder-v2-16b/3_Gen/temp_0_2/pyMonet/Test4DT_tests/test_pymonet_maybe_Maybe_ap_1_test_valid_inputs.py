
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    # Test case 1: Applying a function to a non-empty Maybe
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    result = maybe_some.ap(Maybe(value=5, is_nothing=False))
    assert not result.is_nothing
    assert result.value == 6

    # Test case 2: Applying a function to an empty Maybe
    maybe_empty = Maybe(value=lambda x: x + 1, is_nothing=True)
    result = maybe_empty.ap(Maybe(value=5, is_nothing=False))
    assert result.is_nothing

    # Test case 3: Applying a function to another applicative type with non-empty Maybe
    maybe_some2 = Maybe(value=lambda x: x + 1, is_nothing=False)
    result = maybe_some2.ap(Maybe(value=5, is_nothing=False))
    assert not result.is_nothing
    assert result.value == 6

    # Test case 4: Applying a function to another applicative type with empty Maybe
    maybe_empty2 = Maybe(value=lambda x: x + 1, is_nothing=True)
    result = maybe_empty2.ap(Maybe(value=5, is_nothing=False))
    assert result.is_nothing
