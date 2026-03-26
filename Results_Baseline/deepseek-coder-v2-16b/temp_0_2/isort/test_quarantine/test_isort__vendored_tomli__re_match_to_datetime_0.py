
# Module: isort._vendored.tomli._re
import re
from datetime import datetime, date, timedelta, timezone
from typing import Union, Optional

def match_to_datetime(match: "re.Match") -> Union[datetime, date]:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute, sec = int(hour_str), int(minute_str), int(sec_str)
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    tz: Optional[timezone] = None
    if offset_sign_str:
        tz = cached_tz(offset_hour_str, offset_minute_str, offset_sign_str)
    elif zulu_time:
        tz = timezone.utc
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)

# Test cases for match_to_datetime function

def test_match_to_datetime_with_complete_datetime():
    pattern = r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{6}))?(?:(Z)|([+-]\d{2}:?\d{2}))"
    match = re.match(pattern, "2023-10-15T14:30:00.123456Z")
    assert isinstance(match_to_datetime(match), datetime)
    assert str(match_to_datetime(match)) == "2023-10-15 14:30:00.123456+00:00"

def test_match_to_datetime_with_date_only():
    pattern = r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{6}))?(?:(Z)|([+-]\d{2}:?\d{2}))"
    match = re.match(pattern, "2023-10-15")
    assert isinstance(match_to_datetime(match), date)
    assert str(match_to_datetime(match)) == "2023-10-15"

def test_match_to_datetime_with_time_only():
    pattern = r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{6}))?(?:(Z)|([+-]\d{2}:?\d{2}))"
    match = re.match(pattern, "2023-10-15T14:30:00")
    assert isinstance(match_to_datetime(match), datetime)
    assert str(match_to_datetime(match)) == "2023-10-15 14:30:00"

def test_match_to_datetime_with_invalid_input():
    pattern = r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{6}))?(?:(Z)|([+-]\d{2}:?\d{2}))"
    match = re.match(pattern, "invalid_date")
    try:
        match_to_datetime(match)
    except ValueError as e:
        assert str(e) == "time data 'invalid_date' does not match format '%Y-%m-%d'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_datetime_0
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0.py:33:13: E0602: Undefined variable 'cached_tz' (undefined-variable)


"""