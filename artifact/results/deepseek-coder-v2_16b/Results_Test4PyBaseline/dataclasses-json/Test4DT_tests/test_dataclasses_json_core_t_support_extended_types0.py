
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

# Helper function to safely check if a class is a subclass
def _issubclass_safe(cls, cls_to_check):
    return (isinstance(cls, type) and issubclass(cls, cls_to_check)) or cls == cls_to_check

# Test cases for _support_extended_types function

def test_datetime_conversion():
    now = datetime.now()
    result = _support_extended_types(datetime, now)
    assert isinstance(result, datetime), "Expected a datetime instance"
    assert result == now, "Expected the same datetime object to be returned"

def test_decimal_conversion():
    value = Decimal("123.45")
    result = _support_extended_types(Decimal, "123.45")
    assert isinstance(result, Decimal), "Expected a Decimal instance"
    assert result == value, "Expected the same Decimal value to be returned"

def test_uuid_conversion():
    uuid_value = UUID("123e4567-e89b-12d3-a456-426614174000")
    result = _support_extended_types(UUID, "123e4567-e89b-12d3-a456-426614174000")
    assert isinstance(result, UUID), "Expected a UUID instance"