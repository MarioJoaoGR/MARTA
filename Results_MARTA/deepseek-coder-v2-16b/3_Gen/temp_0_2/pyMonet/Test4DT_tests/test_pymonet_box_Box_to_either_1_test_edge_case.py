
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_to_either():
    # Test with a non-None value
    box = Box(123)
    assert isinstance(box.to_either(), Right)
    assert box.to_either().value == 123

    # Test with None value
    box_none = Box(None)
    assert isinstance(box_none.to_either(), Right)
    assert box_none.to_either().value is None

    # Test with an empty list
    box_empty_list = Box([])
    assert isinstance(box_empty_list.to_either(), Right)
    assert box_empty_list.to_either().value == []
