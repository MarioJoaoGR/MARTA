
from pymonet.either import Right

def test_edge_case():
    right_none = Right(None)
    
    def mapper(x):
        if x is None:
            return 0  # Handle the edge case where the value is None
        else:
            return x + 1
    
    result = right_none.map(mapper)
    assert result.value == 0  # Expected result after mapping when value is None
