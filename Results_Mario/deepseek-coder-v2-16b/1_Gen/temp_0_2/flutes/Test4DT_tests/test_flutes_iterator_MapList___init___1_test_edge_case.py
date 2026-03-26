
import pytest
from flutes.iterator import MapList

def test_edge_case():
    func = lambda x: 0
    lst = []
    
    map_list = MapList(func, lst)
    
    # Since the list is empty, applying any transformation should result in an empty list
    assert len(map_list.list) == 0
