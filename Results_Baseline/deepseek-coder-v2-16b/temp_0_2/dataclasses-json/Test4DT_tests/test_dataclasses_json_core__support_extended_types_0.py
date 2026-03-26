
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

# Test cases for _support_extended_types function

def test_datetime_conversion():
    expected = datetime(2021, 10, 1, 0, 0, tzinfo=timezone.utc)
    result = _support_extended_types(datetime, 1633072800)
    assert isinstance(result, datetime)