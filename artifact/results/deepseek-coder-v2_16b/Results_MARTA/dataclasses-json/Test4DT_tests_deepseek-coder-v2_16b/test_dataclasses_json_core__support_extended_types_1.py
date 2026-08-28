
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

def _support_extended_types(field_type, field_value):
    if isinstance(field_type, type) and issubclass(field_type, (datetime, Decimal, UUID)):
        if isinstance(field_value, field_type):
            return field_value
        elif field_type == datetime:
            tz = datetime.now(timezone.utc).astimezone().tzinfo
            return datetime.fromtimestamp(field_value, tz=tz)
        elif field_type == Decimal:
            return Decimal(field_value) if not isinstance(field_value, Decimal) else field_value
        elif field_type == UUID:
            return UUID(field_value) if not isinstance(field_value, UUID) else field_value
    return field_value

def test_valid_datetime_input():
    dt = datetime.now()
    converted_dt = _support_extended_types(datetime, dt)
    assert isinstance(converted_dt, datetime), "Expected the input to be returned as is since it's already a datetime object."
    assert converted_dt == dt, "Expected no change in the datetime object after conversion."

def test_invalid_datetime_input():
    unix_time = int(datetime.now().timestamp())
    converted_dt = _support_extended_types(datetime, unix_time)
    assert isinstance(converted_dt, datetime), "Expected a datetime object to be created from the Unix timestamp."
    assert converted_dt == datetime.fromtimestamp(unix_time, tz=timezone.utc), "The conversion should match the expected datetime creation from the Unix timestamp."

def test_invalid_uuid_input():
    uuid_str = 'not a valid UUID'
    with pytest.raises(ValueError):
        _support_extended_types(UUID, uuid_str)
