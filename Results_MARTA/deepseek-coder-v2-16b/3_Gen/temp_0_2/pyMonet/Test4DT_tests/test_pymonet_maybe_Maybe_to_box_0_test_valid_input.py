
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value == 42
