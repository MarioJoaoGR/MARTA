
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_empty_list():
    assert curried_map(lambda x: x * 2, []) == []
