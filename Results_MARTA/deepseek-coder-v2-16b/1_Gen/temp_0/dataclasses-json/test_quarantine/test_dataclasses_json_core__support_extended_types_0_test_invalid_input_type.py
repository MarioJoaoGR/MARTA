
import pytest
from dataclasses import dataclass, fields, is_dataclass
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from your_module_name import _support_extended_types  # Replace 'your_module_name' with the actual module name

@pytest.mark.parametrize("field_type, field_value, expected", [
    (datetime, 1633072800, datetime(year=2021, month=10, day=1, tzinfo=timezone.utc)),
    (Decimal, "123.45", Decimal("123.45")),
    (UUID, "123e4567-e89b-12d3-a456-426614174000", UUID("123e4567-e89b-12d3-a456-426614174000")),
    (int, "42", 42),
    (float, "123.45", 123.45),
    (str, 12345, "12345"),
    (bool, True, True)
])
def test_support_extended_types(field_type, field_value, expected):
    result = _support_extended_types(field_type, field_value)
    assert isinstance(result, type(expected)) and result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_0_test_invalid_input_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_invalid_input_type.py:7:0: E0401: Unable to import 'your_module_name' (import-error)

"""