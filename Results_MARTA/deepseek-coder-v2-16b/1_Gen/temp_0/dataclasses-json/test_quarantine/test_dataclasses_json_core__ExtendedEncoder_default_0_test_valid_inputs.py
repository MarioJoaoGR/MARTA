
import json
from datetime import datetime, timezone
from uuid import UUID
from decimal import Decimal
from enum import Enum
import pytest

class MyEnum(Enum):
    VALUE = 'my_value'

encoder = _ExtendedEncoder()

@pytest.mark.parametrize("input_data, expected", [
    ({"key": "value"}, {"key": "value"}),
    (datetime.now(), datetime.now().timestamp()),
    (UUID('123e4567-e89b-12d3-a456-426614174000'), str(UUID('123e4567-e89b-12d3-a456-426614174000'))),
    (MyEnum.VALUE, 'my_value'),
    (Decimal('123.45'), str(Decimal('123.45'))),
    ([1, 2, 3], [1, 2, 3])
])
def test_valid_inputs(input_data, expected):
    assert encoder.default(input_data) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__ExtendedEncoder_default_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__ExtendedEncoder_default_0_test_valid_inputs.py:12:10: E0602: Undefined variable '_ExtendedEncoder' (undefined-variable)

"""