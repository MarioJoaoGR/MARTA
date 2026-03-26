
import pytest
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "my_value"

def test__encode_json_type_list():
    example_list = [1, "string", {"key": "value"}]
    encoded_list = _encode_json_type(example_list)
    assert isinstance(encoded_list, list), "Expected a list but got something else."
    for item in encoded_list:
        assert isinstance(item, (int, str, dict)), f"Item {item} is not of expected type."

def test__encode_json_type_dict():
    example_dict = {"key1": [1, 2], "key2": {"nestedKey": "nestedValue"}}
    encoded_dict = _encode_json_type(example_dict)