
# Assuming string_utils is in the same directory or correctly imported from its parent package
from string_utils import __StringFormatter
import pytest

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(12345)  # This should raise InvalidInputError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_spaces_around_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_2_test_invalid_input.py:3:0: E0611: No name '__StringFormatter' in module 'string_utils' (no-name-in-module)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_2_test_invalid_input.py:7:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)

"""