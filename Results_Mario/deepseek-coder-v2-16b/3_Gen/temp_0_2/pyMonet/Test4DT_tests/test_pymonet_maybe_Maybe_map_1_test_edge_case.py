
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing == True
