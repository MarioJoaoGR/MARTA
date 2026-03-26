
# Module: dataclasses_json.core
import pytest
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json
from typing import Any, Collection, Mapping, Json  # Corrected the typo in 'Json'

# Import the _ExtendedEncoder class from its module
from dataclasses_json.core import _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "enum_value"

encoder = _ExtendedEncoder()

def test_default_for_dict():
    assert encoder.default({"key": "value"}) == {'key': 'value'}

@pytest.mark.parametrize("dt, expected", [
    (datetime.now(), datetime.now().timestamp()),  # The actual timestamp will depend on the current time when this example is run.
])
def test_default_for_datetime(dt, expected):
    assert encoder.default(dt) == expected

@pytest.mark.parametrize("uuid_, expected", [
    (UUID('123e4567-e89b-12d3-a456-426614174000'), '123e4567-e89b-12d3-a456-426614174000')
])
def test_default_for_uuid(uuid_, expected):
    assert encoder.default(uuid_) == expected

@pytest.mark.parametrize("myenum, expected", [
    (MyEnum.VALUE, 'enum_value')
])
def test_default_for_enum(myenum, expected):
    assert encoder.default(myenum) == expected

@pytest.mark.parametrize("decimal_, expected", [
    (Decimal('123.45'), '123.45')
])
def test_default_for_decimal(decimal_, expected):
    assert encoder.default(decimal_) == expected

@pytest.mark.parametrize("sequence, expected", [
    ([1, 2, 3], [1, 2, 3]),
    ("string", "string")
])
def test_default_for_sequence_or_string(sequence, expected):
    assert encoder.default(sequence) == expected

@pytest.mark.parametrize("unsupported_type", [
    1, True, None, float(3.14), complex(1j), b"bytes"
])
def test_default_for_unsupported_types(unsupported_type):
    with pytest.raises(TypeError):  # The exact error depends on the type and implementation of json.JSONEncoder.default
        encoder.default(unsupported_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__ExtendedEncoder_default_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__ExtendedEncoder_default_0.py:9:0: E0611: No name 'Json' in module 'typing' (no-name-in-module)

"""