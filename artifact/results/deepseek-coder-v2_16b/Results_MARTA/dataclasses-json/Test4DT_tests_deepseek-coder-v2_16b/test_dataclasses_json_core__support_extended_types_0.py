
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
            return Decimal(str(field_value)) if not isinstance(field_value, Decimal) else field_value
        elif field_type == UUID:
            return UUID(field_value) if not isinstance(field_value, UUID) else field_value
    else:
        raise TypeError("Conversion to {} not supported for the provided value type.".format(field_type.__name__))

# Test cases
def test_valid_case_datetime():
    dt = datetime.now()
    result = _support_extended_types(datetime, dt)
    assert isinstance(result, datetime), "Expected datetime object"
    assert result == dt, "Expected the same datetime object as input"

def test_valid_case_unix_timestamp():
    unix_time = int(datetime.now().timestamp())
    result = _support_extended_types(datetime, unix_time)
    assert isinstance(result, datetime), "Expected datetime object"
    assert result == datetime.fromtimestamp(unix_time, tz=timezone.utc), "Expected conversion from Unix timestamp to datetime"

def test_valid_case_decimal():
    decimal_val = '123.45'
    result = _support_extended_types(Decimal, decimal_val)
    assert isinstance(result, Decimal), "Expected Decimal object"
    assert str(result) == decimal_val, "Expected the same Decimal value as input"

def test_valid_case_uuid():
    uuid_str = '123e4567-e89b-12d3-a456-426614174000'
    result = _support_extended_types(UUID, uuid_str)
    assert isinstance(result, UUID), "Expected UUID object"
    assert str(result) == uuid_str, "Expected the same UUID string as input"

def test_error_case_unsupported_type():
    with pytest.raises(TypeError):
        result = _support_extended_types(int, 'not a valid UUID')
