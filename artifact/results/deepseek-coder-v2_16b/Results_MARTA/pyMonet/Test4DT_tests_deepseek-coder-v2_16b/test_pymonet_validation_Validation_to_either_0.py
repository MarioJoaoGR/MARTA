
import pytest
from pymonet.validation import Validation

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    validation = Validation(value=42, errors=[])
    assert validation.is_success() == True

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    validation = Validation(value=None, errors=['Error message'])
    assert validation.is_success() == False
