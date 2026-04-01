
import pytest
from flutes.iterator import MapList

def test_edge_case():
    func = lambda x: 0
    lst = []
    
    maplist = MapList(func, lst)
    
    assert len(maplist) == 0
