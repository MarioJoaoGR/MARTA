
import pytest
from pymonet.validation import Validation

def test_valid_input():
    validation = Validation(value=10, errors=[])
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.value == 10

def test_invalid_input():
    with pytest.raises(TypeError):
        Validation().to_either()
