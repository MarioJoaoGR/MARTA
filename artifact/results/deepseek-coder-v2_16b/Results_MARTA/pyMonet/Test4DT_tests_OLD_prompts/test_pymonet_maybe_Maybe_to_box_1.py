
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box
from unittest.mock import patch

# Test to check if Maybe can be transformed into a Box when it has a valid value
def test_valid_value():
    maybe = Maybe(value=42, is_nothing=False)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value == 42

# Test to check if Maybe can be transformed into a Box when it has an invalid value (None)
def test_invalid_value():
    maybe = Maybe(value=None, is_nothing=True)
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value is None

# Test to check if raising TypeError when no value or type is provided
def test_invalid_inputs():
    with pytest.raises(TypeError):
        Maybe(is_nothing=True)  # Should raise TypeError as it lacks a value parameter
