
import re
from datetime import date, datetime, timezone, tzinfo
from typing import Union
from isort.isort/_vendored.tomli._re import match_to_datetime

def test_valid_date():
    match = re.match(r'\d{4}-\d{2}-\d{2}', '2023-01-01')
    assert isinstance(match_to_datetime(match), (datetime, date))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_date
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_date.py:5:17: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_isort__vendored_tomli__re_match_to_datetime_0_test_valid_date, line 5)' (syntax-error)


"""