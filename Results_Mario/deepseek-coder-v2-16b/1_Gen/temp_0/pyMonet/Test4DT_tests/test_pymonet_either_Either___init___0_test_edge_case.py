
import pytest
from pymonet.either import Either, Left, Right

def test_edge_case():
    # Test None as input
    either = Either(None)
    assert isinstance(either, Either)
    assert either.value is None
