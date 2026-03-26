
import pytest
from pymonet.either import Right
from pymonet.maybe import Maybe

def test_valid_input():
    right = Right(value=42)
    maybe = right.to_maybe()
    assert not maybe.is_nothing
    assert maybe.value == 42
