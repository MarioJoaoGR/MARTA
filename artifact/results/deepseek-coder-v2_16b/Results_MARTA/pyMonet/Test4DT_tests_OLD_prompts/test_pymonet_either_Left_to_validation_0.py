
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_valid_input():
    left_instance = Left(value='Valid input')
    validation = left_instance.to_validation()
    assert isinstance(validation, Validation)
    assert not validation.is_success()
    assert validation.errors == ['Valid input']

def test_invalid_input():
    left_instance = Left(value='Invalid input')
    validation = left_instance.to_validation()
    assert isinstance(validation, Validation)
    assert not validation.is_success()
    assert validation.errors == ['Invalid input']

def test_edge_case():
    left_instance = Left(value=None)
    validation = left_instance.to_validation()
    assert isinstance(validation, Validation)
    assert not validation.is_success()
    assert validation.errors == [None]
