
import pytest
from string_utils.manipulation import slugify
from string_utils.exceptions import InvalidInputError

def test_edge_case():
    # Test None input
    with pytest.raises(InvalidInputError) as exc_info:
        slugify(None)
    expected_error_message = "Expected 'str' type, but received 'NoneType'"
    assert str(exc_info.value) == expected_error_message, f"Unexpected error message: {exc_info.value}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_slugify_1_test_edge_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_1_test_edge_case.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_1_test_edge_case.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)


"""