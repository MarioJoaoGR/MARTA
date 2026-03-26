
from pymonet.either import Right, Either
import pytest

def test_edge_case():
    right_none = Right(None)
    
    # Test that mapping over a None value does not raise an exception and returns a new Right instance with None
    mapped_right = right_none.map(lambda x: x if x is not None else None)
    
    assert isinstance(mapped_right, Right)
    assert mapped_right.value is None
