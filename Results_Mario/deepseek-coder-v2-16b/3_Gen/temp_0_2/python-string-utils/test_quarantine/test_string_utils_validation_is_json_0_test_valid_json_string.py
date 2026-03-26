
import pytest
import json
from string_utils.validation import is_full_string

# Assuming JSON_WRAPPER_RE is defined somewhere in your string_utils.validation module
# from string_utils.validation import JSON_WRAPPER_RE

def test_valid_json_string():
    # Test valid JSON strings
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    
    # Test invalid JSON strings and non-string inputs
    assert is_json('{nope}') == False
    assert is_json(None) == False
    assert is_json('') == False
    assert is_json(' ') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_json_0_test_valid_json_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:11:11: E0602: Undefined variable 'is_json' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:12:11: E0602: Undefined variable 'is_json' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:15:11: E0602: Undefined variable 'is_json' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:16:11: E0602: Undefined variable 'is_json' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:17:11: E0602: Undefined variable 'is_json' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:18:11: E0602: Undefined variable 'is_json' (undefined-variable)


"""