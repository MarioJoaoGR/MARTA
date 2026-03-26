
import pytest
from flutes.iterator import MapList

def test_edge_case_empty_list():
    maplist = MapList(lambda x: x * x, [])
    assert list(maplist) == []
