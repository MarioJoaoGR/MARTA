
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

# Test cases for _support_extended_types function

@pytest.mark.parametrize("field_type, field_value, expected", [
    (datetime, 1633072800, datetime(2021, 10, 1, 0, 0, tzinfo=timezone.utc)),
    (Decimal, "12345.6789", Decimal('12345.6789')),
    (UUID, "123e4567-e89b-12d3-a456-426614174000", UUID('123e4567-e89b-12d3-a456-426614174000')),
    (int, "12345", 12345),
    (float, "123.45", 123.45),
    (str, b"hello", "hello"),
    (bool, True, True)
])
def test_support_extended_types(field_type, field_value, expected):
    result = _support_extended_types(field_type, field_value)
    assert isinstance(result, type(expected)), f"Expected {type(expected)}, but got {type(result)}"