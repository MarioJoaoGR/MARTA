
# Module: dataclasses_json.core
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
import json
from enum import Enum

# Helper function to simulate _issubclass_safe for testing
def _issubclass_safe(cls, classinfo):
    return issubclass(cls, classinfo)

# Test cases for _support_extended_types function
@pytest.mark.parametrize("field_type, field_value, expected", [
    # datetime tests
    (datetime, 1633072800, datetime),
    (datetime, "not a timestamp", datetime),
    (datetime, None, None),
    
    # Decimal tests
    (Decimal, "123.45", Decimal("123.45")),
    (Decimal, 123.45, Decimal(123.45)),
    (Decimal, None, None),
    
    # UUID tests
    (UUID, "123e4567-e89b-12d3-a456-426614174000", UUID("123e4567-e89b-12d3-a456-426614174000")),
    (UUID, "not a uuid string", UUID("not a uuid string")),
    (UUID, None, None),
    
    # int tests
    (int, 42, 42),
    (int, "42", 42),
    (int, None, None),
    
    # float tests
    (float, 1.23, 1.23),
    (float, "1.23", 1.23),
    (float, None, None),
    
    # str tests
    (str, "test string", "test string"),
    (str, b"byte string", "byte string"),
    (str, None, None),
    
    # bool tests
    (bool, True, True),
    (bool, False, False),
    (bool, 1, True),
    (bool, 0, False),
    (bool, None, None)
])
def test_support_extended_types(field_type, field_value, expected):
    result = _support_extended_types(field_type, field_value)
    if isinstance(expected, type):
        assert isinstance(result, expected), f"Expected {expected}, but got {type(result)}"
    else:
        assert result == expected, f"Expected {expected}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0.py:54:13: E0602: Undefined variable '_support_extended_types' (undefined-variable)

"""