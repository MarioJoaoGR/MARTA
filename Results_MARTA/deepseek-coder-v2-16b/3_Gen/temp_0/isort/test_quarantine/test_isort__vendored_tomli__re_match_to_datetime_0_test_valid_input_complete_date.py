
import re
from datetime import datetime, date, timedelta, timezone
from typing import Union, Optional, Tuple

def match_to_datetime(match: "re.Match") -> Union[datetime, date]:
    """Convert a `RE_DATETIME` match to either `datetime.datetime` or `datetime.date`.

    This function takes an object of type `re.Match`, which is expected to represent a matched group containing date and time information. The function extracts the year, month, day, hour, minute, second, microsecond, and timezone offset from the match and constructs either a `datetime` or a `date` object based on the available data.

    Parameters:
        match (re.Match): A regular expression match object containing date and time information. The specific structure of this match is expected to conform to a pattern where each component of the date and time can be extracted from its groups.

    Returns:
        Union[datetime, date]: If all necessary components for constructing a `datetime` are present (including hour, minute, second), a `datetime` object is returned with the appropriate timezone information if available. If only year, month, and day are provided without hours, minutes, or seconds, a `date` object is returned.

    Raises:
        ValueError: This exception is raised if the match does not contain valid date or datetime components.

    Examples:
        >>> import re
        >>> match = re.match(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.(\d{6})(Z|[+-]\d{2}:\d{2})", "2023-04-15T12:30:45.123456+01:00")
        >>> match_to_datetime(match)
        datetime.datetime(2023, 4, 15, 12, 30, 45, 123456, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
        
        >>> match = re.match(r"(\d{4})-(\d{2})-(\d{2})", "2023-04-15")
        >>> match_to_datetime(match)
        datetime.date(2023, 4, 15)
        
    Note:
        The function assumes that the input `match` object is a valid regular expression match with all necessary components for constructing either a date or a datetime object. If any of these components are missing or incorrect, a ValueError will be raised.
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
    if offset_sign_str:
        tz = cached_tz(offset_hour_str, offset_minute_str, offset_sign_str)
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_input_complete_date
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_input_complete_date.py:52:13: E0602: Undefined variable 'cached_tz' (undefined-variable)


"""