
import pytest
from flutes.iterator import MapList

def test_maplist_getitem_int():
    ml = MapList(lambda x: x * 2, [1, 2, 3])
    assert ml[0] == 2
    assert ml[1] == 4
    assert ml[2] == 6


def test_maplist_getitem_slice_out_of_range():
    ml = MapList(lambda x: x * 2, [1, 2, 3])
    with pytest.raises(IndexError):
        _ = ml[10]