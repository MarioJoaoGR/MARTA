
import pytest
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
import json
from dataclasses_json.core import _ExtendedEncoder

# Fixture to create an instance of the encoder for each test
@pytest.fixture
def converter():
    return _ExtendedEncoder()

# Test cases for converting different types
def test_default_dict(converter):
    result = converter.default({"key": "value"})
    assert result == {'key': 'value'}

def test_default_list(converter):
    result = converter.default([1, 2, 3])
    assert result == [1, 2, 3]

def test_default_datetime(converter):
    now = datetime.now()
    result = converter.default(now)
    # Check if the timestamp is close to the current time
    assert isinstance(result, float) and abs(result - now.timestamp()) < 0.1

def test_default_uuid(converter):
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    result = converter.default(uuid_obj)
    assert result == '123e4567-e89b-12d3-a456-426614174000'

class MyEnum(Enum):
    VALUE = "my_value"

def test_default_enum(converter):
    enum_obj = MyEnum.VALUE
    result = converter.default(enum_obj)
    assert result == 'my_value'

def test_default_decimal(converter):
    decimal_obj = Decimal('123.45')
    result = converter.default(decimal_obj)
    assert result == '123.45'

# New test case to cover the uncovered line 49
def test_default_unhandled_type(converter):
    class UnhandledType:
        pass
    
    unhandled_object = UnhandledType()
    with pytest.raises(TypeError) as excinfo:
        converter.default(unhandled_object)