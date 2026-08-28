
import pytest
from typesystem.fields import Decimal

def test_serialize_valid_object():
    decimal_instance = Decimal()
    num = 123.45
    result = decimal_instance.serialize(num)
    assert isinstance(result, float), "Expected a float"
    assert result == float(num), "Serialized value does not match expected float"


def test_serialize_none_object():
    decimal_instance = Decimal()
    none_value = None
    result = decimal_instance.serialize(none_value)
    assert result is None, "Expected None for None value"