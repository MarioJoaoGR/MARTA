
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    try_instance = Try(value=None, is_success=False)
    
    # Ensure that the instance was created correctly with None value and False success status
    assert try_instance.value is None
    assert not try_instance.is_success
    
    # Call on_success without a callback should return self
    result = try_instance.on_success(lambda x: print(x))
    assert result == try_instance
