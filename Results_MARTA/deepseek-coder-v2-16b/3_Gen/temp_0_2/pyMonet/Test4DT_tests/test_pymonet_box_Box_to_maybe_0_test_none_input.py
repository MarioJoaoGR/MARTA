
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_none_input():
    box = Box(value=None)
    assert isinstance(box, Box)
    assert box.to_maybe() == Maybe.just(None)
