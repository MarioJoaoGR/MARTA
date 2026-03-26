
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

    another_maybe = Maybe(value="Hello", is_nothing=True)
    assert another_maybe.is_nothing
