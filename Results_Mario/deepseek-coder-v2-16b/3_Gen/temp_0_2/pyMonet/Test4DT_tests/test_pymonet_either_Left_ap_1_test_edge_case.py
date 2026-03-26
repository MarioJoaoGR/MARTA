
import pytest
from pymonet.either import Left

def test_edge_case():
    left_none = Left(None)
    
    # Test that ap method returns a copy of self when called on a Left instance with None value
    assert isinstance(left_none.ap(Left(None)), Left)
