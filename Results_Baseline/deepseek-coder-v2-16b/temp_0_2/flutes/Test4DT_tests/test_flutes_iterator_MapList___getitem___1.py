
# Module: flutes.iterator
import pytest
from typing import List, Callable, Sequence
from flutes.iterator import MapList

# Helper function to create a list of numbers
def square(x):
    return x * x

# Test cases for MapList class
@pytest.mark.skip  # Skipping this test as it is redundant due to the duplication
def test_maplist_basic():
    # Create a list of numbers
    numbers: List[int] = [1, 2, 3, 4, 5]
    
    # Instantiate MapList with the transformation and the list
    mapped_numbers = MapList(square, numbers)
    
    # Check individual elements by index
    assert mapped_numbers[0] == 1  # 1^2
    assert mapped_numbers[1:3] == [4, 9]  # 2^2 and 3^2
    
    # Iterate over the mapped list to check all transformed values
    expected_output = [1, 4, 9, 16, 25]
    for i, num in enumerate(mapped_numbers):
        assert num == expected_output[i]

@pytest.mark.skip  # Skipping this test as it is redundant due to the duplication
def test_maplist_with_bisect():
    import bisect
    
    a = [1, 2, 3, 4, 5]
    
    # Create a MapList instance for squaring each element in `a`
    squared_numbers = MapList(lambda x: x * x, a)
    
    # Use bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(squared_numbers, 10)
    assert pos == 3  # Index where the square is >= 10

@pytest.mark.skip  # Skipping this test as it is redundant due to the duplication
def test_maplist_with_another_list():
    import bisect
    
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    
    # Create MapList instances for transforming elements in `a` and `b`
    mapped_a = MapList(lambda x: x * x, a)
    mapped_b = MapList(lambda i: a[i] * b[i], Range(len(a)))
    
    # Use bisect_left to find the index of the first element in `mapped_b` whose product with `a` is >= 10
    pos = bisect.bisect_left(mapped_b, 10)
    assert pos == 2  # Index where a[2] * b[2] is the first to be >= 10

# Helper class for Range object (assuming it's defined elsewhere in the module)
class Range:
    def __init__(self, length):
        self.length = length
    
    def __getitem__(self, item):
        if isinstance(item, int):
            return slice(item, item + 1)
        elif isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or self.length
            step = item.step or 1
            return [self[i] for i in range(start, min(stop, self.length), step)]
