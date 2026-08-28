
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42
    box_instance = maybe_some.to_box()
    assert isinstance(box_instance, Box)
    assert box_instance.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    box_instance = maybe_none.to_box()
    assert isinstance(box_instance, Box)
    assert box_instance.value is None

# Test invalid input where the function should raise a TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        Maybe().to_box()
