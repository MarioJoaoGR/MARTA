
import pytest
from pymonet.validation import Validation

# Test valid input where Validation is successful
def test_valid_input():
    val = Validation.success(value=10)
    assert not val.errors
    assert val.value == 10

# Test invalid input where Validation should raise TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        Validation()
