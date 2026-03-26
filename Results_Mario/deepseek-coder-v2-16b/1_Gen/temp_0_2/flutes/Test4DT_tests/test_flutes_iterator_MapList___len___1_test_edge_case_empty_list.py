
import pytest
from flutes.iterator import MapList

def test_edge_case_empty_list():
    lst = []
    func = lambda x: x * x
    map_list = MapList(func, lst)
    assert len(map_list) == 0
