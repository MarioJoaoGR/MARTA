
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_edge_case_none():
    maybe = Maybe(value=None, is_nothing=True)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value is None
