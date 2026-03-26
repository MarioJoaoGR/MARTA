
import pytest
from flutes.iterator import MapList
import bisect  # Importing bisect module correctly

# Test Case 1: Transforming a List of Integers by Squaring Each Element
def test_maplist_square():
    # Define a list of integers
    a = [1, 2, 3, 4, 5]
    
    # Create a MapList instance that squares each element in the list
    mapped_list = MapList(lambda x: x * x, a)
    
    # Use bisect.bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    
    assert pos == 3, f"Expected index 3 but got {pos}"

# Test Case 2: Transforming a List of Integers by Multiplying Elements from Two Lists
def test_maplist_multiply():
    # Define two lists of integers
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    
    # Create a MapList instance that multiplies corresponding elements from the two lists
    mapped_list = MapList(lambda i: a[i] * b[i], range(len(a)))
    
    # Use bisect.bisect_left to find the index of the first element whose product is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    
    assert pos == 2, f"Expected index 2 but got {pos}"

# Additional Test Case: Testing with a Different Transformation Function
def test_maplist_custom():
    # Define a list of integers
    c = [3, 6, 9, 12, 15]
    
    # Create a MapList instance that triples each element in the list
    mapped_list = MapList(lambda x: x * 3, c)
    
    # Use bisect.bisect_left to find the index of the first element whose triple is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    