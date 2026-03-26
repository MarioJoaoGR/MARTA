
import pytest
from pymonet.maybe import Maybe

def test_edge_case_none():
    maybe_some = Maybe(value=None, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value is None
