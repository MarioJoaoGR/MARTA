
import pytest
from pymonet.either import Left, Right

def test_edge_case():
    left_none = Left(None)
    assert isinstance(left_none, Left)
    assert left_none.value is None
