
import re
from typing import Callable, Union, Any
from isort._vendored.tomli._re import match_to_number

def test_match_to_number_basic():
    # Test with a string containing an integer part only
    match = re.Match(0, "123", 0)
    parse_float_mock: Callable[[str], Union[int, float]] = lambda x: float(x) if '.' in x else int(x)
    
    # Test with an integer part and a decimal point
    result = match_to_number(match, parse_float_mock)
    assert isinstance(result, int)
    assert result == 123
    
    # Create a new match object with a string containing a decimal point
    match = re.Match(0, "123.456", 0)
    
    # Test with an integer part and a decimal point
    result = match_to_number(match, parse_float_mock)
    assert isinstance(result, float)
    assert result == 123.456
    
    # Create a new match object with a string that cannot be converted to a number
    match = re.Match(0, "abc", 0)
    
    # Test with a non-numeric string
    try:
        match_to_number(match, parse_float_mock)
    except ValueError as e:
        assert str(e) == "could not convert string to float: 'abc'"

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

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_match_to_number_basic.py F [100%]

=================================== FAILURES ===================================
__________________________ test_match_to_number_basic __________________________

    def test_match_to_number_basic():
        # Test with a string containing an integer part only
>       match = re.Match(0, "123", 0)
E       TypeError: cannot create 're.Match' instances

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_match_to_number_basic.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_match_to_number_basic.py::test_match_to_number_basic
============================== 1 failed in 0.10s ===============================
"""