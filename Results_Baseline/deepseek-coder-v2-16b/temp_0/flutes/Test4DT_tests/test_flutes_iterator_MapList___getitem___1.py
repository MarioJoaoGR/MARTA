
import pytest
from flutes.iterator import MapList
import bisect  # Importing here to avoid undefined variable errors

# Test Case 1: Testing __getitem__ with a slice
def test_maplist_slice():
    a = [1, 2, 3, 4, 5]
    transformed_list = MapList(lambda x: x * x, a)
    sliced_list = transformed_list[1:4]  # Slicing from index 1 to 3 (exclusive)
    assert sliced_list == [2**2, 3**2, 4**2]

# Test Case 2: Testing __getitem__ with an integer index out of bounds
def test_maplist_index_out_of_bounds():
    a = [1, 2, 3, 4, 5]
    transformed_list = MapList(lambda x: x * x, a)
    with pytest.raises(IndexError):
        _ = transformed_list[10]  # Index out of bounds should raise an IndexError

# Test Case 3: Testing __getitem__ with a negative index
def test_maplist_negative_index():
    a = [1, 2, 3, 4, 5]
    transformed_list = MapList(lambda x: x * x, a)
    assert transformed_list[-1] == 5**2  # The last element in the list

# Test Case 4: Testing __getitem__ with a slice out of bounds
def test_maplist_slice_out_of_bounds():
    a = [1, 2, 3, 4, 5]
    transformed_list = MapList(lambda x: x * x, a)
    sliced_list = transformed_list[10:]  # Slicing beyond the end of the list
    assert len(sliced_list) == 0  # An empty list should be returned for out-of-bounds slice
