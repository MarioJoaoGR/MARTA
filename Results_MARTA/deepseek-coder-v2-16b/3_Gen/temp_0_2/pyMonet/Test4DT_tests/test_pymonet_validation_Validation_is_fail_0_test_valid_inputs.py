
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    validation = Validation(value=10, errors=[])
    assert validation.is_fail() == False
    assert validation.value == 10
    assert len(validation.errors) == 0
