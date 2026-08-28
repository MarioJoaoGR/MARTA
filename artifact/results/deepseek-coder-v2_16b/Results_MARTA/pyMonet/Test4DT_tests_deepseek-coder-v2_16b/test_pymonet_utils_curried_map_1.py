
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

# Test Scenario 1: Valid Input
def test_valid_input():
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    expected = [2, 4, 6]
    result = curried_map(mapper, collection)
    assert result == expected

# Test Scenario 2: Edge Case with None Input
def test_edge_case_none():
    mapper = lambda x: x * 2
    collection = None
    with pytest.raises(TypeError):
        curried_map(mapper, collection)

# Test Scenario 3: Error Handling for Invalid Mapper Function
def test_error_handling():
    mapper = 'invalid'
    collection = [1, 2, 3]
    with pytest.raises(TypeError):
        curried_map(mapper, collection)
