
import pytest
from typesystem.fields import Decimal

# Scenario 1: Test serialization of a valid numeric object
def test_serialize_valid_numeric():
    decimal_instance = Decimal()
    num = 123.45
    result = decimal_instance.serialize(num)
    assert isinstance(result, float), f"Expected float but got {type(result)}"
    assert result == 123.45, "Unexpected serialization result"

# Scenario 2: Test serialization of a non-numeric object

# Scenario 3: Test serialization of zero
def test_serialize_zero():
    decimal_instance = Decimal()
    zero = 0
    result = decimal_instance.serialize(zero)
    assert isinstance(result, float), f"Expected float but got {type(result)}"
    assert result == 0.0, "Unexpected serialization result"