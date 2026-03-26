
# Module: dataclasses_json.core
# test_extended_encoder.py
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import pytest
from dataclasses_json.core import _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "enum_value"

@pytest.fixture
def encoder():
    return _ExtendedEncoder()

# Test cases for default method
def test_default_dict(encoder):
    result = encoder.default({"key": "value"})
    assert result == {'key': 'value'}

def test_default_datetime(encoder):
    now = datetime.now()
    result = encoder.default(now)
    assert isinstance(result, float), f"Expected a timestamp but got {type(result)}: {result}"

def test_default_uuid(encoder):
    uuid_value = UUID('123e4567-e89b-12d3-a456-426614174000')
    result = encoder.default(uuid_value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}: {result}"
    assert result == '123e4567-e89b-12d3-a456-426614174000'

def test_default_enum(encoder):
    enum_value = MyEnum.VALUE
    result = encoder.default(enum_value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}: {result}"
    assert result == 'enum_value'

def test_default_decimal(encoder):
    decimal_value = Decimal('123.45')
    result = encoder.default(decimal_value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}: {result}"
    assert result == '123.45'

def test_default_list(encoder):
    list_value = [1, 2, 3]
    result = encoder.default(list_value)
    assert isinstance(result, list), f"Expected a list but got {type(result)}: {result}"
    assert result == [1, 2, 3]

def test_default_string(encoder):
    string_value = "string"
    result = encoder.default(string_value)