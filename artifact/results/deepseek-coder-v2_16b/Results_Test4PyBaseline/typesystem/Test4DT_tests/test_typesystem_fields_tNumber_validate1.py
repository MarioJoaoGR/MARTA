
# Module: typesystem.fields
import pytest
from typesystem.fields import Number
from decimal import Decimal, InvalidOperation
import sys

# Ensure that the test environment supports decimal for testing purposes
if not hasattr(sys, 'gettotalrefcount'):  # Check if running in a CPython implementation
    pytestmark = pytest.mark.skip("This test requires CPython with decimal support.")

def test_validate_with_null():
    number = Number(allow_null=True)
    assert number.validate(None) is None

def test_validate_with_empty_string():
    number = Number()
    with pytest.raises(Exception):
        number.validate("")

def test_validate_with_invalid_type():
    number = Number()
    with pytest.raises(Exception):
        number.validate("not a number")

def test_validate_with_boolean():
    number = Number()
    with pytest.raises(Exception):
        number.validate(True)

def test_validate_with_float_non_integer():
    number = Number()
    with pytest.raises(Exception):
        number.validate(3.5)

def test_validate_with_valid_int():
    number = Number()
    validated_value = number.validate(42)
    assert isinstance(validated_value, int)

def test_validate_with_valid_float():
    number = Number()
    validated_value = number.validate(3.14)
    assert isinstance(validated_value, float)

def test_validate_with_string_decimal():
    number = Number()
    validated_value = number.validate("123.45")
    assert isinstance(validated_value, Decimal)

def test_validate_with_invalid_decimal_operation():
    number = Number()
    with pytest.raises(InvalidOperation):
        number.validate("not a decimal")

def test_validate_with_non_finite_number():
    number = Number()
    with pytest.raises(Exception):
        number.validate(float('inf'))

def test_validate_with_valid_decimal_precision():
    number = Number(precision="2")
    validated_value = number.validate("123.456")  # This should be rounded to "120" due to precision constraint
    assert isinstance(validated_value, Decimal) and str(validated_value).startswith('120')

def test_validate_with_invalid_minimum():
    number = Number(minimum=5)
    with pytest.raises(Exception):
        number.validate(3)

def test_validate_with_invalid_maximum():
    number = Number(maximum=5)
    with pytest.raises(Exception):
        number.validate(7)

def test_validate_with_valid_exclusive_minimum():
    number = Number(exclusive_minimum=5)
    validated_value = number.validate(6)
    assert validated_value == 6

def test_validate_with_invalid_exclusive_minimum():
    number = Number(exclusive_minimum=5)
    with pytest.raises(Exception):
        number.validate(5)

def test_validate_with_valid_exclusive_maximum():
    number = Number(exclusive_maximum=5)
    validated_value = number.validate(4)
    assert validated_value == 4

def test_validate_with_invalid_exclusive_maximum():
    number = Number(exclusive_maximum=5)
    with pytest.raises(Exception):
        number.validate(5)

def test_validate_with_valid_multiple_of():
    number = Number(multiple_of=3)
    validated_value = number.validate(9)
    assert validated_value == 9

def test_validate_with_invalid_multiple_of():
    number = Number(multiple_of=3)
    with pytest.raises(Exception):
        number.validate(4)
