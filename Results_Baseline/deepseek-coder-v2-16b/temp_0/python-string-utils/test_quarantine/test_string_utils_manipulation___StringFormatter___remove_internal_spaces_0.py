
# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __StringFormatter
from unittest.mock import patch

# Test cases for __StringFormatter class
def test_init_valid_string():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_init_invalid_type():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

def test_remove_internal_spaces():
    formatter = __StringFormatter("Hello World")
    result = formatter._StringFormatter__remove_internal_spaces(r"(\s+)(.*)(\s+)")
    assert result == "HelloWorld"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:13:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:18:13: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)

"""