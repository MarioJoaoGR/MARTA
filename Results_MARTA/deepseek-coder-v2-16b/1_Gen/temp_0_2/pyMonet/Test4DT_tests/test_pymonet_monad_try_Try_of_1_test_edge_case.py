
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    def unsafe_function(x):
        if x == 0:
            raise ValueError('Input must be non-zero')
        return x + 1
    
    result = Try.of(unsafe_function, 0)
    assert not result.is_success
    assert isinstance(result.value, ValueError)
