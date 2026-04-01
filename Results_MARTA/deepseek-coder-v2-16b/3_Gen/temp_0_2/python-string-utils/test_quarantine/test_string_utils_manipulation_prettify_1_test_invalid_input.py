
import pytest
from string_utils.manipulation import prettify

def test_invalid_input():
    # Test with invalid inputs like numbers and special characters
    assert prettify('12345') == '12345'  # Should not alter numeric input
    assert prettify('!@#$%^&*()') == '!@#$%^&*()'  # Should not alter special character input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with invalid inputs like numbers and special characters
        assert prettify('12345') == '12345'  # Should not alter numeric input
>       assert prettify('!@#$%^&*()') == '!@#$%^&*()'  # Should not alter special character input
E       AssertionError: assert '!@#$%^& * ()' == '!@#$%^&*()'
E         
E         - !@#$%^&*()
E         + !@#$%^& * ()
E         ?        + +

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""