
import pytest
from python_string_utils.manipulation import __StringFormatter, InvalidInputError

def test_none_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(None)
    assert str(excinfo.value) == 'Expected a string but got NoneType'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:3:0: E0401: Unable to import 'python_string_utils.manipulation' (import-error)


"""