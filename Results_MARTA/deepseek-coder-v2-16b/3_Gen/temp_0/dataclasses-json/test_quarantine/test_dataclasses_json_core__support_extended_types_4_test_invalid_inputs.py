
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

def _support_extended_types(field_type, field_value):
    if isinstance(field_type, type) and issubclass(field_type, (datetime, Decimal, UUID, int, float, str, bool)):
        if isinstance(field_value, field_type):
            return field_value
        elif field_type == datetime:
            tz = datetime.now(timezone.utc).astimezone().tzinfo
            return datetime.fromtimestamp(field_value, tz=tz)
        elif field_type == Decimal:
            return Decimal(field_value) if isinstance(field_value, str) else field_value
        elif field_type == UUID:
            return UUID(field_value) if isinstance(field_value, str) else field_value
        elif field_type in (int, float):
            return field_type(field_value)
        elif field_type == str:
            return str(field_value)
        elif field_type == bool:
            if isinstance(field_value, str):
                return True if field_value.lower() in ('true', '1') else False
            else:
                return bool(field_value)
    return field_value

def test_invalid_inputs():
    # Test invalid datetime input
    with pytest.raises(ValueError):
        _support_extended_types(datetime, "not a timestamp")
    
    # Test invalid Decimal input
    with pytest.raises(InvalidOperation):
        _support_extended_types(Decimal, "not a decimal number")
    
    # Test invalid UUID input
    with pytest.raises(ValueError):
        _support_extended_types(UUID, "not a UUID string")
    
    # Test valid datetime input
    assert isinstance(_support_extended_types(datetime, 1633072800), datetime)
    
    # Test valid Decimal input
    assert isinstance(_support_extended_types(Decimal, "123.45"), Decimal)
    
    # Test valid UUID input
    assert isinstance(_support_extended_types(UUID, "123e4567-e89b-12d3-a456-426614174000"), UUID)
    
    # Test valid int input
    assert _support_extended_types(int, 42) == 42
    
    # Test valid float input
    assert _support_extended_types(float, 3.14) == 3.14
    
    # Test valid str input
    assert _support_extended_types(str, "hello") == "hello"
    
    # Test valid bool input
    assert _support_extended_types(bool, True) is True
    assert _support_extended_types(bool, "True") is True
    assert _support_extended_types(bool, 1) is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_4_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_4_test_invalid_inputs.py:35:23: E0602: Undefined variable 'InvalidOperation' (undefined-variable)


"""