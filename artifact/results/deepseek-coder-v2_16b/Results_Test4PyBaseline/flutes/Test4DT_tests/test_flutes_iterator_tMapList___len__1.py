
import pytest
from flutes.iterator import MapList
import bisect  # Importing here since it was not recognized previously

# Test cases for MapList class
def test_maplist_basic():
    # Define a transformation function
    def square(x):
        return x * x

    # Create a list to be wrapped
    original_list = [1, 2, 3, 4, 5]

    # Wrap the list with MapList and perform a transformation
    mapped_list = MapList(square, original_list)

    # Use bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3  # since 4^2 is the first element >= 10

def test_maplist_lambda():
    # Create a list to be wrapped
    original_list = [1, 2, 3, 4, 5]

    # Wrap the list with MapList and perform a transformation using a lambda function
    mapped_list = MapList(lambda x: x * x, original_list)

    # Use bisect_left to find the index of the first element whose square is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3  # since 4^2 is the first element >= 10

def test_maplist_complex():
    # Define a transformation function that uses indices to access elements from two lists
    def multiply_elements(i):
        return original_list[i] * another_list[i]

    # Create the lists to be wrapped
    original_list = [1, 2, 3, 4, 5]
    another_list = [2, 3, 4, 5, 6]

    # Wrap the list with MapList and perform a transformation using the defined function
    mapped_list = MapList(multiply_elements, range(len(original_list)))

    # Use bisect_left to find the index where the product of corresponding elements is >= 10
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 2  # since 3 * 4 is the first pair whose product >= 10

# Additional test case to cover __len__ method in MapList class
def test_maplist_length():
    # Test with a list that has elements transformed by a function
    original_list = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x * x, original_list)
    assert len(mapped_list) == len(original_list)

    # Test with an empty list
    empty_map_list = MapList(lambda x: x * x, [])
    assert len(empty_map_list) == 0

    # Test with a list that has elements transformed by another function
    original_list = [1, 2, 3, 4, 5]
    mapped_list = MapList(lambda x: x + 1, original_list)
    assert len(mapped_list) == len(original_list)
