
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
    
    year, month, day = int(year_str), int(month_str), int(day_str)
    hour, minute, sec = (int(hour_str) if hour_str else None, 
                         int(minute_str) if minute_str else None, 
                         int(sec_str) if sec_str else None)
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    
    if hour is None:
        return date(year, month, day)
    
    tzinfo = None
    if zulu_time:
        tzinfo = timezone.utc
    elif offset_sign_str and offset_hour_str and offset_minute_str:
        hours_offset = int(offset_hour_str) * 3600 + int(offset_minute_str) * 60
        if offset_sign_str == '+':
            tzinfo = timezone(timedelta(hours=hours_offset))
        else:
            tzinfo = timezone(timedelta(hours=-hours_offset))
    
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tzinfo)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:30:9: E0602: Undefined variable 'offset_sign_str' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:30:29: E0602: Undefined variable 'offset_hour_str' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:30:49: E0602: Undefined variable 'offset_minute_str' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:31:27: E0602: Undefined variable 'offset_hour_str' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:31:57: E0602: Undefined variable 'offset_minute_str' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_datetime_input.py:32:11: E0602: Undefined variable 'offset_sign_str' (undefined-variable)


"""