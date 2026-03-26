
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    box = maybe.to_box()
    assert not maybe.is_nothing
    assert box.value == 42
