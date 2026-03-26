
import pytest
from string_utils.manipulation import __StringFormatter
from custom_exceptions import InvalidInputError

def test_valid_input():
    # Test with a valid string input
    try:
        formatter = __StringFormatter("valid string")
        assert isinstance(formatter, __StringFormatter)
        assert formatter.input_string == "valid string"
    except InvalidInputError as e:
        pytest.fail(f"Unexpected InvalidInputError raised: {e}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_right_space_only_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_0_test_valid_input.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""