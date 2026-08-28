
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    left_instance = Left(value='An error occurred')
    validation_monad = left_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.errors == ['An error occurred']

# Test invalid input where Maybe is empty (is_nothing is True)
def test_invalid_input():
    with pytest.raises(TypeError):
        left_instance = Left()
