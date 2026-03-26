
import pytest
from datetime import timezone, timedelta

def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
    sign = 1 if sign_str == "+" else -1
    return timezone(
        timedelta(
            hours=sign * int(hour_str),
            minutes=sign * int(minute_str),
        )
    )

def test_edge_cases():
    # Test with None values
    assert cached_tz(None, None, None) is None
    
    # Test with empty strings
    assert cached_tz("", "", "") is None
    
    # Test with invalid hour and minute values
    with pytest.raises(ValueError):
        cached_tz("13", "60", "+")  # Invalid minute value
        
    with pytest.raises(ValueError):
        cached_tz("-5", "-30", "+")  # Negative hours and minutes
        
    # Test with invalid sign
    assert cached_tz("5", "30", "X") is None  # Invalid sign

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__re_cached_tz_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None values
>       assert cached_tz(None, None, None) is None

isort/Test4DT_tests/test_isort__vendored_tomli__re_cached_tz_0_test_edge_cases.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hour_str = None, minute_str = None, sign_str = None

    def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
        sign = 1 if sign_str == "+" else -1
        return timezone(
            timedelta(
>               hours=sign * int(hour_str),
                minutes=sign * int(minute_str),
            )
        )
E       TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

isort/Test4DT_tests/test_isort__vendored_tomli__re_cached_tz_0_test_edge_cases.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_cached_tz_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""