
import pytest
from pymonet.maybe import Maybe

# Test initialization of Maybe with a value
def test_init_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test initialization of Maybe without a value
def test_init_without_value():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing