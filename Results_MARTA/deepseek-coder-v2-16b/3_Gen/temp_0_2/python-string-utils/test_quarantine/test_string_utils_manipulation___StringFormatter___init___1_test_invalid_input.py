
import pytest
from string_utils.manipulation import is_string, InvalidInputError
from __StringFormatter import __StringFormatter

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert isinstance(exc_info.value, InvalidInputError)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___init___1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___1_test_invalid_input.py:4:0: E0401: Unable to import '__StringFormatter' (import-error)


"""