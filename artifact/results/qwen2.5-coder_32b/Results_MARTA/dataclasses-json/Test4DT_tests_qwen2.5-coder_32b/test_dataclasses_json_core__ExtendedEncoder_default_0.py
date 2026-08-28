
import json
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
from collections.abc import Collection, Mapping
from dataclasses_json.core import _ExtendedEncoder

def _isinstance_safe(obj, cls):
    try:
        return isinstance(obj, cls)
    except Exception:
        return False

class Color(Enum):
    RED = 1
    GREEN = 2

# Test cases for _ExtendedEncoder.default method

def test_extended_encoder_list():
    encoder = _ExtendedEncoder()
    example_list = [1, 2, 3]
    serialized_list = json.dumps(example_list, cls=_ExtendedEncoder)
    assert serialized_list == "[1, 2, 3]"

def test_extended_encoder_dict():
    encoder = _ExtendedEncoder()
    example_dict = {'key': 'value'}
    serialized_dict = json.dumps(example_dict, cls=_ExtendedEncoder)
    assert serialized_dict == '{"key": "value"}'

def test_extended_encoder_datetime():
    encoder = _ExtendedEncoder()
    example_datetime = datetime(2023, 1, 1)
    serialized_datetime = json.dumps(example_datetime, cls=_ExtendedEncoder)
    assert serialized_datetime == "1672531200.0"

def test_extended_encoder_uuid():
    encoder = _ExtendedEncoder()
    example_uuid = UUID('12345678-1234-5678-1234-567812345678')
    serialized_uuid = json.dumps(example_uuid, cls=_ExtendedEncoder)
    assert serialized_uuid == '"12345678-1234-5678-1234-567812345678"'

def test_extended_encoder_enum():
    encoder = _ExtendedEncoder()
    example_enum = Color.RED
    serialized_enum = json.dumps(example_enum, cls=_ExtendedEncoder)
    assert serialized_enum == "1"

def test_extended_encoder_decimal():
    encoder = _ExtendedEncoder()
    example_decimal = Decimal('10.5')
    serialized_decimal = json.dumps(example_decimal, cls=_ExtendedEncoder)
    assert serialized_decimal == '"10.5"'
