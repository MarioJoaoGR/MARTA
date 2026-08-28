
import pytest
from typesystem.fields import Number, ValidationError
from decimal import Decimal

# Scenario 1: Test standard input with valid schema definitions

# Scenario 2: Test validation of invalid integer input
def test_validate_invalid_integer():
    number = Number(minimum=0, maximum=10)
    with pytest.raises(ValidationError):
        number.validate(15)

# Scenario 3: Test validation of invalid float input
def test_validate_invalid_float():
    number = Number(minimum=0, maximum=10)
    with pytest.raises(ValidationError):
        number.validate(15.5)

# Scenario 4: Test validation of invalid multiple_of input
def test_validate_invalid_multiple_of():
    number = Number(minimum=0, maximum=100, multiple_of=3)
    with pytest.raises(ValidationError):
        number.validate(10)

# Scenario 5: Test validation of null not allowed input
def test_validate_null_not_allowed():
    number = Number(minimum=0, maximum=10, allow_null=False)
    with pytest.raises(ValidationError):
        number.validate(None)

# Scenario 6: Test validation of strict mode for type checking

# Scenario 7: Test validation of infinite value input
def test_validate_infinite():
    number = Number(minimum=0, maximum=10)
    with pytest.raises(ValidationError):
        number.validate(float('inf'))