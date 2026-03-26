
import pytest
from datetime import datetime
from dataclasses_json.core import _ExtendedEncoder
import json
from decimal import Decimal
from uuid import UUID
from enum import Enum

def test_valid_datetime():
    encoder = _ExtendedEncoder()
    now = datetime.now()
    
    # Test datetime object
    assert isinstance(encoder.default(now), (int, float)), "Expected a timestamp for datetime object"
    
    # Test UUID object
    uuid_obj = UUID('123e4567-e89b-12d3-a456-426614174000')
    assert isinstance(encoder.default(uuid_obj), str), "Expected a string representation for UUID object"
    
    # Test Decimal object
    decimal_obj = Decimal('123.45')
    assert isinstance(encoder.default(decimal_obj), str), "Expected a string representation for Decimal object"
    
    # Test list
    test_list = [1, 2, 3]
    assert isinstance(encoder.default(test_list), list), "Expected a JSON list for list input"
    
    # Test dictionary
    test_dict = {'key': 'value'}
    assert isinstance(encoder.default(test_dict), dict), "Expected a JSON dictionary for dictionary input"
    
    # Test other types (should fallback to default behavior)
    class MyEnum(Enum):
        VALUE = 'enum_value'
    my_enum_obj = MyEnum.VALUE
    assert isinstance(encoder.default(my_enum_obj), str), "Expected a string representation for Enum object"
    
    # Test unsupported type (should fallback to default behavior)
    class UnsupportedType:
        pass
    unsupported_obj = UnsupportedType()
    with pytest.raises(TypeError):
        encoder.default(unsupported_obj)
