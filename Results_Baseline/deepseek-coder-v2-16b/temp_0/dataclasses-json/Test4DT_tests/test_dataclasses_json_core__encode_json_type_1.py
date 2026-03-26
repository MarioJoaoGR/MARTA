
import pytest
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "my_value"

def test__encode_json_type_non_json():
    # Test with a non-Json.__args__ type that should be handled by default encoder
    value = {"key": "value"}
    encoded_value = _encode_json_type(value)
    assert isinstance(encoded_value, dict), "Expected a dictionary but got something else."
    for k, v in encoded_value.items():
        if isinstance(v, (list, dict)):
            assert isinstance(v, list), "Nested items should be lists."
        else:
            assert not isinstance(v, (list, dict)), f"Item {v} is not of expected type."

def test__encode_json_type_non_json_with_default():
    # Test with a non-Json.__args__ type that should be handled by default encoder and ensure it uses the provided default encoder
    value = {"key": "value"}
    encoded_value = _encode_json_type(value, default=lambda x: str(x))
    assert isinstance(encoded_value, dict), "Expected a dictionary but got something else."
    for v in encoded_value.values():
        assert isinstance(v, str), f"Item {v} is not of expected type (str)."

def test__encode_json_type_custom_encoder():
    # Test with a custom object that has an associated encoder
    class CustomEncoder:
        def default(self, obj):
            if isinstance(obj, list):
                return [_encode_json_type(i) for i in obj]
            elif isinstance(obj, dict):
                return {k: _encode_json_type(v) for k, v in obj.items()}
            else:
                return str(obj)
    
    value = [1, "string", {"key": "value"}]
    encoded_value = _encode_json_type(value, default=CustomEncoder().default)