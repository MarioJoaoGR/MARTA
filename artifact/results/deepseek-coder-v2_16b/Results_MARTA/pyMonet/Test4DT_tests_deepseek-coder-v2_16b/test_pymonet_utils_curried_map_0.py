
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

# Test Scenario 1: Test standard input with a lambda function and a list of numbers
def test_valid_input():
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    expected = [2, 4, 6]
    result = curried_map(mapper, collection)
    assert result == expected, f"Expected {expected}, but got {result}"

# Test Scenario 2: Test with an empty list to check how the function handles no elements
def test_edge_case_empty_list():
    mapper = lambda x: x * 2
    collection = []
    expected = []
    result = curried_map(mapper, collection)
    assert result == expected, f"Expected {expected}, but got {result}"

# Test Scenario 3: Test with a non-callable mapper and an invalid collection type to check error handling
def test_invalid_input():
    mapper = 'not callable'
    collection = [1, 2, 3]
    with pytest.raises(TypeError):
        curried_map(mapper, collection)
