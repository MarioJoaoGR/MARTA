
import pytest
from dataclasses_json.core import _ExtendedEncoder
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
import json

class MyEnum(Enum):
    VALUE = "enum_value"

def test_encode_dictionary():
    encoder = _ExtendedEncoder()
    dictionary_to_encode = {"key": "value"}
    encoded_dict = encoder.default(dictionary_to_encode)
    assert encoded_dict == {'key': 'value'}

def test_encode_datetime():
    encoder = _ExtendedEncoder()
    now = datetime.now()
    encoded_datetime = encoder.default(now)
    assert isinstance(encoded_datetime, float), f"Expected a timestamp but got {type(encoded_datetime)}"

def test_encode_uuid():
    encoder = _ExtendedEncoder()
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    encoded_uuid = encoder.default(uuid_obj)
    assert encoded_uuid == '123e4567-e89b-12d3-a456-426614174000'

def test_encode_enum():
    encoder = _ExtendedEncoder()
    encoded_enum = encoder.default(MyEnum.VALUE)
    assert encoded_enum == 'enum_value'

def test_encode_decimal():
    encoder = _ExtendedEncoder()
    decimal_val = Decimal('123.45')
    encoded_decimal = encoder.default(decimal_val)
    assert encoded_decimal == '123.45'
