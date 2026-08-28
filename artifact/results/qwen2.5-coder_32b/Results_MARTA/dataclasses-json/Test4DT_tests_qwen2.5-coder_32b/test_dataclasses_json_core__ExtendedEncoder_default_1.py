
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

# Test file for _ExtendedEncoder.default method
def test__ExtendedEncoder_default_basic():
    encoder = _ExtendedEncoder()

    # Test with a list
    example_list = [1, 2, 3]
    assert encoder.default(example_list) == [1, 2, 3]

    # Test with a dictionary
    example_dict = {'key': 'value'}
    assert encoder.default(example_dict) == {'key': 'value'}

    # Test with a datetime object
    example_datetime = datetime(2023, 1, 1)
    assert encoder.default(example_datetime) == example_datetime.timestamp()

    # Test with a UUID object
    example_uuid = UUID('12345678-1234-5678-1234-567812345678')
    assert encoder.default(example_uuid) == str(example_uuid)

    # Test with an Enum value
    example_enum = Color.RED
    assert encoder.default(example_enum) == example_enum.value

    # Test with a Decimal object
    example_decimal = Decimal('10.5')
    assert encoder.default(example_decimal) == str(example_decimal)
