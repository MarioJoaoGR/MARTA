
import pytest
from python_string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        bad_formatter = __StringFormatter(12345)
    assert str(excinfo.value) == "Expected 'str', received 'int'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_invalid_input.py:3:0: E0401: Unable to import 'python_string_utils.manipulation' (import-error)


"""