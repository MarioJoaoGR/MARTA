
from pymonet.either import Right, Either
import pytest

def test_invalid_input():
    right_string = Right('string')
    
    def mapper(x):
        return int(x)  # Correctly convert string to integer
    
    with pytest.raises(ValueError):
        right_string.map(mapper)
