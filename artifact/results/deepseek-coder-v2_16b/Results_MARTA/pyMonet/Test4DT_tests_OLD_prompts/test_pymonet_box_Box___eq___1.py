
import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_valid_input():
    box = Box(42)
    validation = box.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.value == 42

def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_validation()
