
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    empty_maybe = Maybe(None, True)
    assert empty_maybe.get_or_else(0) == 0
