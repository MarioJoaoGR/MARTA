
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing == True
    mapped_maybe = maybe.map(lambda x: x + 1)
    assert mapped_maybe.is_nothing == True
