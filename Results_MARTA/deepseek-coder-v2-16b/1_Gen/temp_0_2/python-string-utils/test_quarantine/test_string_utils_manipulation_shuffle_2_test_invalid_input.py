
import pytest
from string_utils import shuffle
from string_utils.exceptions import InvalidInputError

def test_invalid_input():
    # Test that an InvalidInputError is raised when a non-string input is provided
    with pytest.raises(InvalidInputError) as exc_info:
        shuffle(12345)
    
    assert str(exc_info.value) == "Expected 'str', received '<class 'int'>'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_shuffle_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_2_test_invalid_input.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_2_test_invalid_input.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)


"""