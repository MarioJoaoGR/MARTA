
import pytest
from pymonet.validation import Validation

# Test valid input where Validation has a value and no errors
def test_valid_input():
    val = Validation(value=10, errors=[])
    assert not val.errors
    assert val.value == 10

# Test edge case where Validation is empty (no value and some errors)
def test_edge_case():
    val = Validation(value=None, errors=['Error message'])
    assert val.errors == ['Error message']
    assert val.value is None

# Test equality between two valid Validations with the same values and errors
def test_validation_equality():
    val1 = Validation(value=42, errors=[])
    val2 = Validation(value=42, errors=[])
    assert val1 == val2

# Test inequality between a valid Validation and an invalid one with different values or errors
def test_validation_inequality():
    val_valid = Validation(value=42, errors=[])
    val_invalid = Validation(value=None, errors=['Error message'])
    assert not (val_valid == val_invalid)
