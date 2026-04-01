
import pytest
from superstring.superstring import SuperStringLower

def test_error_handling():
    with pytest.raises(AttributeError):
        s = SuperStringLower("Hello, World!")
        s.upper()  # This should raise an AttributeError because the base attribute is not a string in this context

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_1_test_error_handling.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_1_test_error_handling.py::test_error_handling
============================== 1 failed in 0.04s ===============================
"""