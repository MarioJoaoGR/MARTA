
import pytest
from superstring.superstring import SuperStringLower, SuperStringBase

def test_valid_input():
    base = "Hello World"
    lower_instance = SuperStringLower(base)
    
    converted_string = lower_instance.upper()
    assert converted_string._base == "HELLO WORLD"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        base = "Hello World"
        lower_instance = SuperStringLower(base)
    
        converted_string = lower_instance.upper()
>       assert converted_string._base == "HELLO WORLD"
E       AttributeError: 'str' object has no attribute '_base'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_valid_input.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""