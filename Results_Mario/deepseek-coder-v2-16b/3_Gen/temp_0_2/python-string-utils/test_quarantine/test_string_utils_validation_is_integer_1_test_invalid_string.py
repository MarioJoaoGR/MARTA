
import pytest
from string_utils.validation import is_integer

def test_invalid_string():
    with pytest.raises(ValueError):
        is_integer('invalid')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_1_test_invalid_string.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_string ______________________________

    def test_invalid_string():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_1_test_invalid_string.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_1_test_invalid_string.py::test_invalid_string
============================== 1 failed in 0.03s ===============================
"""