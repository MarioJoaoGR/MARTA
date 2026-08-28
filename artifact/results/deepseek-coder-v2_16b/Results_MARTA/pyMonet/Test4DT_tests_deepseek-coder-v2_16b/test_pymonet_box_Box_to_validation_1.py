
import pytest
from pymonet.box import Box
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    box = Box(42)
    validation = box.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success
    assert validation.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    with pytest.raises(TypeError):
        box = Box()
