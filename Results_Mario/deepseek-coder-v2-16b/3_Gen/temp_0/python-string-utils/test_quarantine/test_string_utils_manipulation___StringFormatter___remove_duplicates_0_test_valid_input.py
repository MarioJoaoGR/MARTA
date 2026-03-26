
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    # Test that an invalid input raises the expected error
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(12345)  # This should raise InvalidInputError
    assert str(excinfo.value) == "Expected 'str', received 'int'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that an invalid input raises the expected error
        with pytest.raises(InvalidInputError) as excinfo:
            __StringFormatter(12345)  # This should raise InvalidInputError
>       assert str(excinfo.value) == "Expected 'str', received 'int'"
E       assert 'Expected "st...eceived "int"' == "Expected 'st...eceived 'int'"
E         
E         - Expected 'str', received 'int'
E         ?          ^   ^           ^   ^
E         + Expected "str", received "int"
E         ?          ^   ^           ^   ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_valid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""