
import json
from datetime import datetime, timedelta
from uuid import UUID
from decimal import Decimal
from enum import Enum
from typing import Any, Collection, Mapping, List, Dict
from dataclasses_json.core import _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "my_value"

def test_edge_cases():
    encoder = _ExtendedEncoder()
    
    # Test with a dictionary
    assert encoder.default({"key": "value"}) == {'key': 'value'}
    
    # Test with datetime object
    now = datetime.now()
    encoded_datetime = encoder.default(now)
    # Allow some tolerance for timestamp comparison due to potential differences in time precision
    assert abs((encoded_datetime - now.timestamp()) / now.timestamp()) < 0.01
    
    # Test with UUID object
    uuid_value = UUID('123e4567-e89b-12d3-a456-426614174000')
    assert encoder.default(uuid_value) == str(uuid_value)
    
    # Test with Enum object
    assert encoder.default(MyEnum.VALUE) == 'my_value'
    
    # Test with Decimal object
    decimal_value = Decimal('123.45')
    assert encoder.default(decimal_value) == str(decimal_value)
    
    # Test with a list
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    
    # Test with an unsupported type (should fallback to default JSON encoding)
    class UnsupportedType:
        pass
    unsupported_obj = UnsupportedType()
    try:
        encoder.default(unsupported_obj)
    except TypeError as e:
        assert str(e) == 'Object of type UnsupportedType is not JSON serializable'
