
import pytest
from datetime import datetime, timezone
from dataclasses_json.utils import _timestamp_to_dt_aware

def test_basic_usage():
    now = datetime.now(timezone.utc)
    aware_dt = _timestamp_to_dt_aware(now.timestamp())
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"

def test_specific_timestamp():
    specific_timestamp = 1672502400.0  # Example timestamp for January 1, 2023, at midnight UTC
    aware_dt = _timestamp_to_dt_aware(specific_timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"