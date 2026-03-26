
import pytest
from datetime import datetime, timezone, timedelta
from dataclasses_json.utils import _timestamp_to_dt_aware

def test_timestamp_to_dt_aware_current_time():
    now = datetime.now(timezone.utc)
    unix_timestamp = now.timestamp()
    aware_dt = _timestamp_to_dt_aware(unix_timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"
    assert aware_dt.utcoffset() is not None, "Expected timezone information"

def test_timestamp_to_dt_aware_specific_time():
    specific_time = datetime.now() - timedelta(hours=1)
    unix_timestamp = specific_time.timestamp()
    aware_dt = _timestamp_to_dt_aware(unix_timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"
    assert aware_dt.utcoffset() is not None, "Expected timezone information"
    assert aware_dt.replace(tzinfo=None) == specific_time.astimezone(timezone.utc).replace(tzinfo=None), "Datetime objects should match"

def test_timestamp_to_dt_aware_negative_timestamp():
    negative_timestamp = -3600
    aware_dt = _timestamp_to_dt_aware(negative_timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"
    assert aware_dt.utcoffset() is not None, "Expected timezone information"
    # Convert the negative timestamp to a positive Unix timestamp representing seconds since the epoch
    expected_timestamp = (datetime(1970, 1, 1).replace(tzinfo=timezone.utc) - timedelta(hours=1)).timestamp()
    assert aware_dt.timestamp() == pytest.approx(expected_timestamp), "Timestamp should be correctly converted from negative to positive"

def test_timestamp_to_dt_aware_zero_timestamp():
    zero_timestamp = 0.0
    aware_dt = _timestamp_to_dt_aware(zero_timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"
    assert aware_dt.utcoffset() is not None, "Expected timezone information"
    # Convert the zero timestamp to a datetime representing January 1, 1970 in UTC
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    assert aware_dt == epoch, "Zero timestamp should be correctly converted to datetime for Unix epoch"
