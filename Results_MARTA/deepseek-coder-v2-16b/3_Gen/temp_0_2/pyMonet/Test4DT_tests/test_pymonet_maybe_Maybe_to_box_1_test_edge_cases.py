
import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing == True
    
    # Test conversion to Box when is_nothing is True
    box_from_maybe_none = maybe_none.to_box()
    assert isinstance(box_from_maybe_none, Box)
    assert box_from_maybe_none.value is None
    
    # Test empty list (not None but still an edge case to consider)
    empty_list = Maybe(value=[], is_nothing=True)
    assert empty_list.is_nothing == True
    
    # Test conversion to Box when is_nothing is True for empty list
    box_from_empty_list = empty_list.to_box()
    assert isinstance(box_from_empty_list, Box)
    assert box_from_empty_list.value is None
    
    # Test non-empty list (not edge case but good for testing)
    non_empty_list = Maybe(value=[1, 2, 3], is_nothing=False)
    assert non_empty_list.is_nothing == False
    
    # Test conversion to Box when is_nothing is False
    box_from_non_empty_list = non_empty_list.to_box()
    assert isinstance(box_from_non_empty_list, Box)
    assert box_from_non_empty_list.value == [1, 2, 3]
