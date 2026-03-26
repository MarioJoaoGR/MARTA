
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert str(exc_info.value) == "'int' is not a valid input, must be a string."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(InvalidInputError) as exc_info:
            formatter = __StringFormatter(12345)
>       assert str(exc_info.value) == "'int' is not a valid input, must be a string."
E       assert 'Expected "st...eceived "int"' == "'int' is not... be a string."
E         
E         - 'int' is not a valid input, must be a string.
E         + Expected "str", received "int"

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""