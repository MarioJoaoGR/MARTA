
import pytest
from pymonet.maybe import Maybe

def test_empty_maybe():
    maybe_none = Maybe(value=None, is_nothing=True)
    filtered_maybe = maybe_none.filter(lambda x: x > 10)
    assert maybe_none.is_nothing is True
    assert filtered_maybe.is_nothing is True
