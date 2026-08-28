
import pytest
from dataclasses_json.core import _ExtendedEncoder
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
import json

# Test scenario 1: Encoding a dictionary
def test_encode_dictionary():
    encoder = _ExtendedEncoder()
    test_data = {"key": "value"}
    encoded_data = encoder.default(test_data)
    assert isinstance(encoded_data, dict), f"Expected dict but got {type(encoded_data)}"
    assert encoded_data == {'key': 'value'}, f"Unexpected encoded data: {encoded_data}"

# Test scenario 2: Encoding a datetime object
def test_encode_datetime():
    encoder = _ExtendedEncoder()
    test_data = datetime.now()
    encoded_data = encoder.default(test_data)
    assert isinstance(encoded_data, float), f"Expected float (timestamp) but got {type(encoded_data)}"

# Test scenario 3: Encoding a UUID object
def test_encode_uuid():
    encoder = _ExtendedEncoder()
    test_data = UUID('123e4567-e89b-12d3-a456-426614174000')
    encoded_data = encoder.default(test_data)
    assert isinstance(encoded_data, str), f"Expected str but got {type(encoded_data)}"
    assert encoded_data == '123e4567-e89b-12d3-a456-426614174000', f"Unexpected encoded data: {encoded_data}"

# Test scenario 4: Encoding an Enum member
class MyEnum(Enum):
    VALUE = "enum_value"
def test_encode_enum():
    encoder = _ExtendedEncoder()
    test_data = MyEnum.VALUE
    encoded_data = encoder.default(test_data)
    assert isinstance(encoded_data, str), f"Expected str but got {type(encoded_data)}"
    assert encoded_data == 'enum_value', f"Unexpected encoded data: {encoded_data}"

# Test scenario 5: Encoding a Decimal number
def test_encode_decimal():
    encoder = _ExtendedEncoder()
    test_data = Decimal('123.45')
    encoded_data = encoder.default(test_data)
    assert isinstance(encoded_data, str), f"Expected str but got {type(encoded_data)}"
    assert encoded_data == '123.45', f"Unexpected encoded data: {encoded_data}"

# Test scenario 6: Encoding a string