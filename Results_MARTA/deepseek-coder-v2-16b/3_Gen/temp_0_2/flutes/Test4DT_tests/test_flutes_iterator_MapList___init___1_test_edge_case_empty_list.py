
import pytest
from flutes.iterator import MapList

def test_edge_case_empty_list():
    func = lambda x: x * x
    lst = []
    
    map_list = MapList(func, lst)
    
    assert list(map_list) == []
