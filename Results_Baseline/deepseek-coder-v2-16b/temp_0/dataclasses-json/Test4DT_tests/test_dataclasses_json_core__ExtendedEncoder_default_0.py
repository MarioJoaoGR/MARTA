
import pytest
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json

# Assuming the module name is dataclasses_json.core
from dataclasses_json.core import _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "my_value"

encoder = _ExtendedEncoder()

def test_default_with_mapping():
    assert encoder.default({"key": "value"}) == {'key': 'value'}

def test_default_with_datetime():
    now = datetime.now()
    result = encoder.default(now)
    # Since the timestamp depends on the current time, we cannot directly compare it to a fixed value.
    # We can only check if the result is a number (timestamp in seconds since epoch).
    assert isinstance(result, (int, float))

def test_default_with_uuid():
    uuid_value = UUID('123e4567-e89b-12d3-a456-426614174000')
    result = encoder.default(uuid_value)
    assert result == '123e4567-e89b-12d3-a456-426614174000'

def test_default_with_enum():
    enum_value = MyEnum.VALUE
    result = encoder.default(enum_value)
    assert result == 'my_value'

def test_default_with_decimal():
    decimal_value = Decimal('123.45')
    result = encoder.default(decimal_value)
    assert result == '123.45'

def test_default_with_sequence():
    sequence_value = [1, 2, 3]
    result = encoder.default(sequence_value)
    assert result == [1, 2, 3]

def test_default_fallback():
    non_supported_object = object()
    # Since the default method uses Python's JSONEncoder, it should handle objects not explicitly supported by _ExtendedEncoder.
    with pytest.raises(TypeError):
        encoder.default(non_supported_object)
