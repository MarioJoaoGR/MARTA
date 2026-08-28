
# Module: dataclasses_json.mm
# test_dataclasses_json_mm.py
from dataclasses import dataclass
import datetime
from dataclasses_json.mm import _TimestampField, ValidationError

def test__serialize_with_valid_datetime():
    timestamp_field = _TimestampField()
    now = datetime.datetime.now()
    result = timestamp_field._serialize(now, attr="timestamp", obj=None)
    assert isinstance(result, float), "Expected a float timestamp"
    assert result == now.timestamp(), f"Expected {now.timestamp()} but got {result}"

def test__serialize_with_none():
    timestamp_field = _TimestampField()
    result = timestamp_field._serialize(None, attr="timestamp", obj=None)
    assert result is None, "Expected None for a non-required field when value is None"

def test__serialize_with_required_and_none():
    timestamp_field = _TimestampField()
    try:
        timestamp_field._serialize(None, attr="timestamp", obj=None)
    except ValidationError as e:
        assert str(e.messages) == "This field is required.", f"Expected 'This field is required.' but got {e.messages}"

def test__serialize_with_valid_datetime_and_required():
    timestamp_field = _TimestampField()
    now = datetime.datetime.now()
    result = timestamp_field._serialize(now, attr="timestamp", obj=None)
    assert isinstance(result, float), "Expected a float timestamp"
    assert result == now.timestamp(), f"Expected {now.timestamp()} but got {result}"
