
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

# Test scenarios
def test_valid_input():
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    expected = [2, 4, 6]
    result = curried_map(mapper, collection)
    assert result == expected

def test_edge_case_empty_list():
    mapper = lambda x: x * 2
    collection = []
    expected = []
    result = curried_map(mapper, collection)
    assert result == expected

def test_invalid_input_none():
    mapper = lambda x: x * 2
    collection = None
    with pytest.raises(TypeError):
        curried_map(mapper, collection)
