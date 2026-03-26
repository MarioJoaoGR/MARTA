
from dataclasses_json.core import _ExtendedEncoder
import json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import pytest

class MyEnum(Enum):
    VALUE = "my_value"

def test_valid_inputs():
    encoder = _ExtendedEncoder()
    
    # Test with a dictionary
    assert encoder.default({"key": "value"}) == {'key': 'value'}
    
    # Test with a datetime object
    now = datetime.now()
    encoded_time = encoder.default(now)
    assert isinstance(encoded_time, float), f"Expected float timestamp but got {type(encoded_time)}"
    
    # Test with a UUID object
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    assert encoder.default(uuid_obj) == str(uuid_obj)
    
    # Test with an enum object
    assert encoder.default(MyEnum.VALUE) == 'my_value'
    
    # Test with a Decimal number
    decimal_num = Decimal('123.45')
    assert encoder.default(decimal_num) == str(decimal_num)
    
    # Test with a list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
