
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None input
    try_instance_none = Try(None, False)
    assert try_instance_none.is_success == False
    assert try_instance_none.value is None
    
    # Test with empty list input
    try_instance_empty = Try([], False)
    assert try_instance_empty.is_success == False
    assert len(try_instance_empty.value) == 0
