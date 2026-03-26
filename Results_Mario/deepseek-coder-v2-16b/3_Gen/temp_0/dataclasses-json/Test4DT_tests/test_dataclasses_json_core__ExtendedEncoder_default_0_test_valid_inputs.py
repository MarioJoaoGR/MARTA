
from dataclasses_json.core import _ExtendedEncoder
import json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum

class MyEnum(Enum):
    VALUE = "my_value"

def test_valid_inputs():
    encoder = _ExtendedEncoder()
    
    # Test with a dictionary
    assert encoder.default({"key": "value"}) == {'key': 'value'}
    
    # Test with a datetime object
    now = datetime.now()
    encoded_time = encoder.default(now)
    assert isinstance(encoded_time, float), "Expected a timestamp"
    
    # Test with a UUID object
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    encoded_uuid = encoder.default(uuid_obj)
    assert isinstance(encoded_uuid, str), "Expected a string representation of UUID"
    
    # Test with an enum object
    encoded_enum = encoder.default(MyEnum.VALUE)
    assert encoded_enum == 'my_value', "Expected the enum value as a string"
    
    # Test with a Decimal object
    decimal_obj = Decimal('123.45')
    encoded_decimal = encoder.default(decimal_obj)
    assert isinstance(encoded_decimal, str), "Expected a string representation of Decimal"
    
    # Test with a list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
