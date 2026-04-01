
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

def test_support_extended_types():
    # Test datetime conversion
    field_type = datetime
    field_value = 1633072800  # Timestamp representing a specific date and time
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, datetime), "Expected datetime object"
    
    # Test Decimal conversion
    field_type = Decimal
    field_value = "123.45"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, Decimal), "Expected Decimal object"
    
    # Test UUID conversion
    field_type = UUID
    field_value = "123e4567-e89b-12d3-a456-426614174000"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, UUID), "Expected UUID object"
    
    # Test int conversion
    field_type = int
    field_value = "42"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, int), "Expected int object"
    
    # Test float conversion
    field_type = float
    field_value = "123.45"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, float), "Expected float object"
    
    # Test str conversion
    field_type = str
    field_value = 42
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, str), "Expected str object"
    
    # Test bool conversion
    field_type = bool
    field_value = "True"
    res = _support_extended_types(field_type, field_value)
    assert isinstance(res, bool), "Expected bool object"
    
    # Test unsupported type
    field_type = list
    field_value = 42
    res = _support_extended_types(field_type, field_value)
    assert res == field_value, "Expected original value for unsupported type"
