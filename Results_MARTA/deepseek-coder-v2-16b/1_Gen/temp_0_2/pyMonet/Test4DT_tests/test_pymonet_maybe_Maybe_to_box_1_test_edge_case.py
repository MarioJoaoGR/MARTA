
import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=False)
    maybe_empty = Maybe(value=None, is_nothing=True)
    
    assert isinstance(maybe_none.to_box(), Box)
    assert maybe_none.to_box().value is None
    
    assert isinstance(maybe_empty.to_box(), Box)
    assert maybe_empty.to_box().value is None
