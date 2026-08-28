
import pytest
from dataclasses_json.mm import _TimestampField, ValidationError

def test_deserialize_valid_timestamp_not_required():
    ts_field = _TimestampField(required=False)
    timestamp = 1633072800.0  # Corresponds to October 1, 2021, 00:00:00 UTC
    aware_datetime = ts_field._deserialize(timestamp, None, {})
    assert aware_datetime is not None

def test_deserialize_valid_timestamp_required():
    ts_field_required = _TimestampField(required=True)
    timestamp = 1633072800.0  # Corresponds to October 1, 2021, 00:00:00 UTC
    aware_datetime = ts_field_required._deserialize(timestamp, None, {})
    assert aware_datetime is not None

def test_deserialize_none_not_required():
    ts_field = _TimestampField(required=False)
    aware_datetime = ts_field._deserialize(None, None, {})
    assert aware_datetime is None

def test_error_handling_required_field():
    ts_field_required = _TimestampField(required=True)
    value = None
    with pytest.raises(ValidationError) as excinfo:
        ts_field_required._deserialize(value, None, {})
    assert str(excinfo.value) == "Missing data for required field."
