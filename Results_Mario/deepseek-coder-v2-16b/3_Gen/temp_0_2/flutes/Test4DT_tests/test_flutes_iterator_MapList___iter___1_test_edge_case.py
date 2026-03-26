
from flutes.iterator import MapList
import pytest
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

@pytest.fixture
def map_list():
    return MapList(lambda x: x * 2, [1, 2, 3, 4, 5])

def test_map_list_iteration(map_list):
    result = []
    for item in map_list:
        result.append(item)
    assert result == [2, 4, 6, 8, 10]
