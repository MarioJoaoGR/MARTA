
import pytest
from copy import deepcopy

class Indices:
    _slice = slice(None)

    def __getitem__(self, item):
        assert isinstance(item, slice)
        result = deepcopy(self)
        result._slice = item
        return result

def test_valid_slices():
    indices = Indices()
    new_indices = indices[1:5]
    assert new_indices._slice == slice(1, 5, None)

def test_edge_cases():
    indices = Indices()
    full_slice = indices[:]
    reverse_slice = indices[::-1]
    empty_slice = indices[0:0]
    assert full_slice._slice == slice(None, None, None)
    assert reverse_slice._slice == slice(None, None, -1)
    assert empty_slice._slice == slice(0, 0, None)

def test_invalid_input():
    indices = Indices()
    with pytest.raises(AssertionError):
        _ = indices[1]
    with pytest.raises(AssertionError):
        _ = indices['a']
