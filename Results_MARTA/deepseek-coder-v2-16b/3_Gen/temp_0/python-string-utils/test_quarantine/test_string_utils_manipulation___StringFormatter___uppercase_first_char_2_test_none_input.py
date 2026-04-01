
import pytest
from string_utils.manipulation import __StringFormatter

def test_none_input():
    formatter = __StringFormatter(None)
    assert isinstance(formatter, __StringFormatter), "Expected an instance of __StringFormatter"
    with pytest.raises(InvalidInputError) as excinfo:
        formatter.__uppercase_first_char("some_string")
    assert str(excinfo.value) == "'NoneType' object is not callable", "Expected InvalidInputError for None input"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_2_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_2_test_none_input.py:8:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""