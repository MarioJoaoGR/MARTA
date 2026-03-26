
import re
from datetime import datetime, date, timedelta, timezone
from typing import Union

def match_to_datetime(match: "re.Match") -> Union[datetime, date]:
    """Convert a `RE_DATETIME` match to either `datetime.datetime` or `datetime.date`.

    This function takes an object of type `re.Match`, which is expected to represent a matched group containing date and time information. The function extracts the year, month, day, hour, minute, second, microsecond, and timezone offset from the match and constructs either a `datetime` or a `date` object based on whether any time components are present.

    Parameters:
        match (re.Match): A regular expression match object containing date and time information. The specific format of this match is not detailed here as it depends on the regex pattern used to define `RE_DATETIME`.

    Returns:
        Union[datetime, date]: If the match contains any time components (hour, minute, second), a `datetime` object is returned with the specified year, month, day, hour, minute, second, and microsecond. If there are no time components, a `date` object is returned with the specified year, month, and day.

    Raises:
        ValueError: If the match does not correspond to a valid date or datetime, this exception is raised.
    """
    groups = match.groups()
    if len(groups) != 10:
        raise ValueError("Invalid match object")
    
    year_str, month_str, day_str, hour_str, minute_str, sec_str, micros_str, zulu_time, offset_sign_str, offset_hour_str, offset_minute_str = groups
    
    year, month, day = int(year_str), int(month_str), int(day_str)
    hour, minute, sec = (int(hour_str) if hour_str else 0), int(minute_str), int(sec_str)
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    
    if zulu_time:
        tz = timezone.utc
    elif offset_sign_str and offset_hour_str and offset_minute_str:
        sign = -1 if offset_sign_str == '-' else 1
        hours, minutes = int(offset_hour_str), int(offset_minute_str)
        tz = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
    else:
        tz = None
    
    if hour is not None or minute is not None or sec is not None:
        return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)
    else:
        return date(year, month, day)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.08s =============================
"""