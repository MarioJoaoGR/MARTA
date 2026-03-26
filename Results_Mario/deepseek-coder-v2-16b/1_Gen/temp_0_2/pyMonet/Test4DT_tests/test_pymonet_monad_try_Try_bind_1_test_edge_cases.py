
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value and False is_success
    failure = Try(None, False)
    assert failure.value is None
    assert not failure.is_success
    
    # Test bind method with a function that returns a new Try instance
    def example_function(x):
        return Try(x + "!", True)
    
    # Bind should return the original Try instance since is_success is False
    result = failure.bind(example_function)
    assert result.value is None
    assert not result.is_success
