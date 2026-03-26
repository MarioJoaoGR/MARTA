
import pytest
from dataclasses import dataclass, fields, is_dataclass
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

def test_invalid_inputs():
    # Test with unsupported type
    field_type = list
    field_value = "not a valid list"
    assert _support_extended_types(field_type, field_value) == field_value

    # Test with datetime type and valid timestamp
    field_type = datetime
    field_value = 1633072800  # Timestamp representing a specific date and time
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, datetime), "Expected datetime object"

    # Test with Decimal type and valid string value
    field_type = Decimal
    field_value = "123.45"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, Decimal), "Expected Decimal object"

    # Test with UUID type and valid string value
    field_type = UUID
    field_value = "123e4567-e89b-12d3-a456-426614174000"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, UUID), "Expected UUID object"

    # Test with int type and valid string value
    field_type = int
    field_value = "42"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, int), "Expected integer value"
