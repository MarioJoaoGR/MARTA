
import re
from datetime import datetime, date, timedelta, timezone
from typing import Union, Optional

def match_to_datetime(match: "re.Match") -> Union[datetime, date]:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    groups = match.groups()
    year_str, month_str, day_str = groups[0], groups[1], groups[2]
    hour_str, minute_str, sec_str = groups[3], groups[4], groups[5]
    micros_str = groups[6]
    zulu_time = groups[7]
    offset_sign_str, offset_hour_str, offset_minute_str = None, None, None
    if len(groups) == 10:
        offset_sign_str, offset_hour_str, offset_minute_str = groups[8], groups[9], groups[10]

    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute, sec = int(hour_str), int(minute_str), int(sec_str)
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0

    if offset_sign_str:
        tz = timezone(timedelta(hours=int(offset_hour_str), minutes=int(offset_minute_str)))
    elif zulu_time:
        tz = timezone.utc
    else:
        tz = None

    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)

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
============================ no tests ran in 0.05s =============================
"""