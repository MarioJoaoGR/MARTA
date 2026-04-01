
import pytest
from flutes.iterator import MapList
from typing import List, Callable

# Define the square function as given in the setup
def square(x: int) -> int: return x * x

# Test data
test_list = [1, 2, 3, 4, 5]

def test_valid_input():
    # Create an instance of MapList with the square function and the test list
    map_list = MapList(square, test_list)
    
    # Convert the MapList to a list to easily compare with the expected result
    transformed_list = list(map_list)
    
    # Expected result after applying the square function to each element in the test list
    expected_result = [1, 4, 9, 16, 25]
    
    # Assert that the transformed list matches the expected result
    assert transformed_list == expected_result
