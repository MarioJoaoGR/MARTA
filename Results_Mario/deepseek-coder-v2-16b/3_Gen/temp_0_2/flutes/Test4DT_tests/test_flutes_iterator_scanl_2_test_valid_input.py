
import pytest
from flutes.iterator import scanl

def test_valid_input():
    # Test case 1: Summing up elements of a list
    result = list(scanl(lambda x, y: x + y, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
    
    # Test case 2: Multiplying elements of a list
    result = list(scanl(lambda x, y: x * y, [1, 2, 3, 4]))
    assert result == [1, 2, 6, 24]
    
    # Test case 3: Using scanl with a generator expression
    result = list(scanl(lambda x, y: x + y, (x for x in range(1, 5))))
    assert result == [1, 3, 6, 10]
    
    # Test case 4: Using scanl with an empty iterable
    try:
        list(scanl(lambda x, y: x + y, []))
    except RuntimeError as e:
        assert str(e) == "generator raised StopIteration"
