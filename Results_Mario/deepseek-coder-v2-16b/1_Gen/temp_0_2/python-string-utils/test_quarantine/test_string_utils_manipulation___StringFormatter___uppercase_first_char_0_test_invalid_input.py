
from string_utils.manipulation import InvalidInputError
import pytest

def test_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        formatter = __StringFormatter(None)
    assert str(excinfo.value) == "Invalid input: None"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_invalid_input.py:7:20: E0602: Undefined variable '__StringFormatter' (undefined-variable)


"""