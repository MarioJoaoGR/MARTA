
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _issubclass_safe

def _support_extended_types(field_type, field_value):
    if _issubclass_safe(field_type, datetime):
        # FIXME this is a hack to deal with mm already decoding
        # the issue is we want to leverage mm fields' missing argument
        # but need this for the object creation hook
        if isinstance(field_value, datetime):
            res = field_value
        else:
            tz = datetime.now(timezone.utc).astimezone().tzinfo
            res = datetime.fromtimestamp(field_value, tz=tz)
    elif _issubclass_safe(field_type, Decimal):
        res = (field_value
               if isinstance(field_value, Decimal)
               else Decimal(field_value))
    elif _issubclass_safe(field_type, UUID):
        res = (field_value
               if isinstance(field_value, UUID)
               else UUID(field_value))
    else:
        res = field_value
    return res

def test__support_extended_types_basic():
    # Test conversion of timestamp to datetime
    timestamp = 1633072800
    converted_datetime = _support_extended_types(datetime, timestamp)
    expected_datetime = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone()
    assert converted_datetime == expected_datetime

    # Test conversion of string to Decimal
    string_decimal = "123.45"
    converted_decimal = _support_extended_types(Decimal, string_decimal)
    assert converted_decimal == Decimal("123.45")

    # Test conversion of string to UUID
    uuid_string = "123e4567-e89b-12d3-a456-426614174000"
    converted_uuid = _support_extended_types(UUID, uuid_string)
    assert converted_uuid == UUID("123e4567-e89b-12d3-a456-426614174000")

    # Test no conversion for string
    example_str = "example"
    unchanged_value = _support_extended_types(str, example_str)
    assert unchanged_value == "example"
