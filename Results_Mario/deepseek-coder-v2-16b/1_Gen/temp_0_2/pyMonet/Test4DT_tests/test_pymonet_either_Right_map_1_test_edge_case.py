
import pytest
from pymonet.either import Right

def test_edge_case():
    # Setup
    right_none = Right(None)
    
    # Function under test
    def mapper(x):
        return x + 1
    
    # Expected behavior
    expected_output = None
    
    # Actual test
    with pytest.raises(TypeError):
        result = right_none.map(mapper)
