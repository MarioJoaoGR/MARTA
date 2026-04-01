
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Right

def test_none_input():
    right = Right(None)
    maybe = right.to_maybe()
    assert isinstance(maybe, Maybe)
    assert not maybe.is_nothing
    assert maybe.value is None
