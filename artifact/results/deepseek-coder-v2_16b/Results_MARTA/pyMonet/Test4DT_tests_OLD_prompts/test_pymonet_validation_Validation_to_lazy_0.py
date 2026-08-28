
import pytest
from pymonet.validation import Validation

def test_valid_initialization():
    val = Validation(10, [])
    assert isinstance(val, Validation)
    assert val.value == 10
    assert val.errors == []

def test_invalid_input():
    with pytest.raises(TypeError):
        Validation()
