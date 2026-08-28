
import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_valid_input():
    box = Box(42)
    validation = box.to_validation()
    assert isinstance(validation, Validation), f"Expected instance of Validation but got {type(validation)}"
    assert validation.is_success(), "Validation should be successful"
    assert validation.value == 42, f"Expected value to be 42 but got {validation.value}"

def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_validation()
