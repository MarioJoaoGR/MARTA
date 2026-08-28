
import pytest
from uuid import UUID
from datetime import datetime, timezone
from decimal import Decimal
from dataclasses_json.core import _support_extended_types

def test_valid_uuid_input():
    uuid_str = "123e4567-e89b-12d3-a456-426614174000"
    res = _support_extended_types(UUID, uuid_str)
    assert isinstance(res, UUID), f"Expected UUID but got {type(res)}"


def test_datetime_from_timestamp():
    unix_time = int(datetime.now().timestamp())
    res = _support_extended_types(datetime, unix_time)
    assert isinstance(res, datetime), f"Expected datetime but got {type(res)}"

def test_decimal_from_string():
    decimal_str = "123.45"
    res = _support_extended_types(Decimal, decimal_str)
    assert isinstance(res, Decimal), f"Expected Decimal but got {type(res)}"

def test_no_conversion_needed():
    dt = datetime.now()
    res = _support_extended_types(datetime, dt)
    assert isinstance(res, datetime), f"Expected datetime but got {type(res)}"