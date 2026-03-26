
import pytest
from string_utils.validation import is_string

def test_invalid_type():
    assert not is_string('foo')  # should pass because 'foo' is a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_string_1_test_invalid_type.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_type _______________________________

    def test_invalid_type():
>       assert not is_string('foo')  # should pass because 'foo' is a string
E       AssertionError: assert not True
E        +  where True = is_string('foo')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_string_1_test_invalid_type.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_string_1_test_invalid_type.py::test_invalid_type
============================== 1 failed in 0.03s ===============================
"""