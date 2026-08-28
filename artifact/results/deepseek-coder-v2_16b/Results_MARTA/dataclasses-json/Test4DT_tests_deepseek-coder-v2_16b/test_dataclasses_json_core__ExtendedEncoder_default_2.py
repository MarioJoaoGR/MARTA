
import pytest
from dataclasses_json.core import _ExtendedEncoder
from datetime import datetime, timedelta
from uuid import UUID
from enum import Enum
from decimal import Decimal
import json

# Test encoding a dictionary
def test_encode_dictionary():
    encoder = _ExtendedEncoder()
    dictionary_to_encode = {"key": "value"}
    encoded_dict = encoder.default(dictionary_to_encode)
    assert isinstance(encoded_dict, dict)
    assert encoded_dict == {"key": "value"}

# Test encoding a datetime object
def test_encode_datetime():
    encoder = _ExtendedEncoder()
    now = datetime.now()
    encoded_datetime = encoder.default(now)
    # Assuming the timestamp method returns a float, we can assert its type and value
    assert isinstance(encoded_datetime, (float, int))
    # For simplicity, let's check if it's within a reasonable range of now
    assert abs((encoded_datetime - now.timestamp())) < 1

# Test encoding a UUID object
def test_encode_uuid():
    encoder = _ExtendedEncoder()
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    encoded_uuid = encoder.default(uuid_obj)
    assert isinstance(encoded_uuid, str)
    assert encoded_uuid == '123e4567-e89b-12d3-a456-426614174000'

# Test encoding an Enum member
class MyEnum(Enum):
    VALUE = "enum_value"
def test_encode_enum():
    encoder = _ExtendedEncoder()
    encoded_enum = encoder.default(MyEnum.VALUE)
    assert isinstance(encoded_enum, str)
    assert encoded_enum == 'enum_value'

# Test encoding a Decimal number
def test_encode_decimal():
    encoder = _ExtendedEncoder()
    decimal_val = Decimal('123.45')
    encoded_decimal = encoder.default(decimal_val)
    assert isinstance(encoded_decimal, str)
    assert encoded_decimal == '123.45'

# Test encoding a non-supported type (should raise TypeError)
def test_encode_none():
    encoder = _ExtendedEncoder()
    none_value = None
    with pytest.raises(TypeError):
        encoder.default(none_value)
