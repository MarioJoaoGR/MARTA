
import pytest
from typing import Callable, Collection
from flutes.structure import map_structure  # Assuming this module exists in your project

# Example function to use with map_structure for testing
def square(x):
    return x ** 2

# Test cases for map_structure
def test_map_structure():
    # Testing list
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Testing tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Testing dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Testing set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}
    
    # Testing nested structure (list within a tuple)
    assert map_structure(square, ([1, 2], [3, 4])) == ([1, 4], [9, 16])
    
    # Testing function applied directly if not collection type
    assert map_structure(square, 5) == 25

# Run the test case
if __name__ == "__main__":
    pytest.main()
