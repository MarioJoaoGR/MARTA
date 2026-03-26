
# Module: string_utils.manipulation
# string_utils.manipulation/test_string_formatter.py
from string_utils.manipulation import __StringFormatter
import pytest
from pytest import raises as pytest_raises  # Renamed for clarity and consistency with the rest of the test case

class InvalidInputError(Exception):
    pass  # This is a placeholder for the exception definition, which was missing in the original code

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_invalid_input_type():
    with pytest_raises(InvalidInputError) as excinfo:
        __StringFormatter(12345)
    assert str(excinfo.value) == "Expected 'str', received 'int'"

def test_fix_saxon_genitive():
    formatter = __StringFormatter("The quick brown fox")
    fixed_string = formatter._StringFormatter__fix_saxon_genitive(r"\b(\w+)\s*")
    assert fixed_string == "Thequickbrownfox"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0.py:22:19: E1101: Instance of '__StringFormatter' has no '_StringFormatter__fix_saxon_genitive' member (no-member)

"""