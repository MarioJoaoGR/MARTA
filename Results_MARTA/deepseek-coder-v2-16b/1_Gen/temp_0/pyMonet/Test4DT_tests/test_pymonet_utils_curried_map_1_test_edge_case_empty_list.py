
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_edge_case_empty_list():
    def square(x):
        return x ** 2
    
    assert curried_map(square, []) == []
