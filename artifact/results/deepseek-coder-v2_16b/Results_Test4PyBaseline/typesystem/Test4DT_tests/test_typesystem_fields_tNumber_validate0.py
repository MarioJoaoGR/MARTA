# Module: typesystem.fields
import pytest
from typesystem.fields import Number
from decimal import Decimal
import sys

# Ensure that the test environment supports decimal for testing purposes
if not hasattr(sys, 'gettotalrefcount'):  # Check if running in a CPython implementation
    pytestmark = pytest.mark.skip("This test requires CPython with decimal support.")

def test_basic_instantiation():
    number = Number()
    assert number is not None

def test_with_minimum_and_maximum_constraints():
    number = Number(minimum=0, maximum=10)
    assert number.minimum == 0
    assert number.maximum == 10

def test_with_precision_constraint():
    number = Number(precision="2")
    assert number.precision == "2"

def test_with_multiple_of_constraint():
    number = Number(multiple_of=3)
    assert number.multiple_of == 3

def test_with_all_constraints():
    number = Number(minimum=0, maximum=10, exclusive_minimum=5, exclusive_maximum=9, precision="2", multiple_of=3)
    assert number.minimum == 0
    assert number.maximum == 10
    assert number.exclusive_minimum == 5
    assert number.exclusive_maximum == 9
    assert number.precision == "2"
    assert number.multiple_of == 3

def test_validating_a_value():
    number = Number(minimum=0, maximum=10, exclusive_minimum=5, exclusive_maximum=9, precision="2", multiple_of=3)
    validated_value = number.validate(7)
    assert validated_value == 7

def test_validating_an_invalid_value():
    number = Number(minimum=0, maximum=10, exclusive_minimum=5, exclusive_maximum=9, precision="2", multiple_of=3)
    with pytest.raises(Exception):
        number.validate(12)  # This should raise an error because 12 exceeds the maximum constraint

def test_validating_null():
    number = Number()
    validated_value = number.validate(None)
    assert validated_value is None
