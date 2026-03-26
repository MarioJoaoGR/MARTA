
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringSubstring

def test_valid_substring():
    base_str = SuperStringBase()
    result = base_str.substring(7, 12)
    
    assert isinstance(result, SuperStringSubstring), "Expected a SuperStringSubstring instance"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_substring.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_substring _____________________________

    def test_valid_substring():
        base_str = SuperStringBase()
        result = base_str.substring(7, 12)
    
>       assert isinstance(result, SuperStringSubstring), "Expected a SuperStringSubstring instance"
E       AssertionError: Expected a SuperStringSubstring instance
E       assert False
E        +  where False = isinstance(<superstring.superstring.SuperString object at 0x7f651ad68610>, SuperStringSubstring)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_substring.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_valid_substring.py::test_valid_substring
============================== 1 failed in 0.04s ===============================
"""