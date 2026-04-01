
from unittest.mock import patch
from string_utils.manipulation import __placeholder_key
import pytest

@pytest.mark.parametrize("input_string", [None, "", "test"])
def test_none_input(input_string):
    with pytest.raises(InvalidInputError):
        if input_string is None:
            __StringFormatter(input_string)
        else:
            formatter = __StringFormatter(input_string)
            assert formatter.input_string == input_string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:3:0: E0611: No name '__placeholder_key' in module 'string_utils.manipulation' (no-name-in-module)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:8:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:10:12: E0602: Undefined variable '__StringFormatter' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:12:24: E0602: Undefined variable '__StringFormatter' (undefined-variable)


"""