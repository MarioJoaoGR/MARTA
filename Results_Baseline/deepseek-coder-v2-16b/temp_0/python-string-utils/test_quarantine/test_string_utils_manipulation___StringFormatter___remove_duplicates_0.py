
# Module: string_utils.manipulation
# string_utils.manipulation/test_string_formatter.py
from string_utils.manipulation import __StringFormatter
import pytest
from pytest import raises as pytest_raises  # Renamed for consistency with the corrected test case

class InvalidInputError(Exception):
    pass

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_invalid_input_type():
    with pytest_raises(InvalidInputError) as excinfo:
        __StringFormatter(12345)
    assert str(excinfo.value) == "Expected 'str', received 'int'"

def test_remove_duplicates():
    formatter = __StringFormatter("hellooo")
    result = formatter._StringFormatter__remove_duplicates(''.join(re.findall(r'(.)(\1+)', 'hellooo')))
    assert result == "hello"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0.py:22:13: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_duplicates' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0.py:22:67: E0602: Undefined variable 're' (undefined-variable)

"""