
import pytest
from flutes.iterator import scanl
import operator

def test_valid_input():
    # Test with a list of integers and an initial value
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test with a list of strings without an initial value
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']
    
    # Test with a list of integers and no initial value
    result = list(scanl(operator.add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
    
    # Test with an empty iterable
    with pytest.raises(RuntimeError):
        result = list(scanl(operator.add, []))
