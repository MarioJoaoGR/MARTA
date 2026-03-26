
import pytest
from pymonet.maybe import Maybe

def test_edge_case_none():
    maybe = Maybe(value=None, is_nothing=False)
    filtered_maybe = maybe.filter(lambda x: True)
    assert filtered_maybe.is_nothing is False
    assert filtered_maybe.value is None
