
import pytest
from unittest.mock import patch
from pymonet.validation import Validation
from pymonet.either import Right

# Test scenario 1: test_valid_input
def test_valid_input():
    right_instance = Right(10)
    with patch('pymonet.validation.Validation.success', return_value=Validation(10, [])):
        validation_monad = right_instance.to_validation()
        assert validation_monad.value == 10

# Test scenario 2: test_edge_case
def test_edge_case():
    right_instance = Right(None)
    with patch('pymonet.validation.Validation.success', return_value=Validation(None, [])):
        validation_monad = right_instance.to_validation()
        assert validation_monad.value == None

# Test scenario 3: test_invalid_input
def test_invalid_input():
    right_instance = Right('string')
    with patch('pymonet.validation.Validation.success', return_value=Validation('string', [])):
        validation_monad = right_instance.to_validation()
        assert validation_monad.value == 'string'
