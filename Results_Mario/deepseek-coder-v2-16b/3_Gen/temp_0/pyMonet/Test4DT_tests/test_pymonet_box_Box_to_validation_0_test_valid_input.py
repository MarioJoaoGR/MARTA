
import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_valid_input():
    box = Box(123)
    validation_monad = box.to_validation()
    
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success() is True
    assert validation_monad.value == 123
