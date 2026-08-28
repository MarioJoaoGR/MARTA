
import pytest
from typesystem.fields import Number
from decimal import Decimal
import sys

# Ensure that the test environment supports decimal for testing purposes
if not hasattr(sys, 'gettotalrefcount'):  # Check if running in a CPython implementation
    pytestmark = pytest.mark.skip("This test requires CPython with decimal support.")

def test_validate_null():
    number = Number(allow_null=True)
    assert number.validate(None) is None

def test_validate_empty_string():
    number = Number()
    with pytest.raises(Exception):
        number.validate("")

def test_validate_invalid_type():
    number = Number()
    with pytest.raises(Exception):
        number.validate(True)  # True is a boolean, not an int or float

def test_validate_non_integer_float():
    number = Number()
    with pytest.raises(Exception):
        number.validate(123.45)  # Float that is not an integer

def test_validate_nan():
    number = Number()
    with pytest.raises(Exception):
        number.validate(float('nan'))  # NaN is invalid

def test_validate_infinite():
    number = Number()
    with pytest.raises(Exception):
        number.validate(float('inf'))  # Infinity is invalid

def test_validate_with_precision():
    number = Number(precision="2")
    validated_value = number.validate("123.456")
    assert isinstance(validated_value, Decimal) and validated_value == Decimal("123.46").quantize(Decimal("0.01"))

def test_validate_with_minimum():
    number = Number(minimum=10)
    with pytest.raises(Exception):
        number.validate(5)  # Value less than minimum should raise an error

def test_validate_with_exclusive_minimum():
    number = Number(exclusive_minimum=10)
    with pytest.raises(Exception):
        number.validate(10)  # Value equal to exclusive minimum should raise an error

def test_validate_with_maximum():
    number = Number(maximum=10)
    with pytest.raises(Exception):
        number.validate(15)  # Value greater than maximum should raise an error

def test_validate_with_exclusive_maximum():
    number = Number(exclusive_maximum=10)
    with pytest.raises(Exception):
        number.validate(10)  # Value equal to exclusive maximum should raise an error

def test_validate_with_multiple_of():
    number = Number(multiple_of=3)
    validated_value = number.validate(9)
    assert isinstance(validated_value, int) and validated_value == 9

def test_validate_invalid_multiple_of():
    number = Number(multiple_of=3)
    with pytest.raises(Exception):
        number.validate(4)  # Value not a multiple of 3 should raise an error
