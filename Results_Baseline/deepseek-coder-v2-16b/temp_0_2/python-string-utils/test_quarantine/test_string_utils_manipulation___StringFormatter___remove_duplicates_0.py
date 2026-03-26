
# Module: string_utils.manipulation
# test_string_utils.py
from string_utils.manipulation import __StringFormatter
import pytest

def is_string(input_string):
    return isinstance(input_string, str)

class InvalidInputError(Exception):
    pass

@pytest.fixture
def valid_formatter():
    return __StringFormatter("Hello, World!")

@pytest.fixture
def invalid_formatter():
    with pytest.raises(InvalidInputError):
        yield __StringFormatter(12345)

def test_valid_init(valid_formatter):
    assert valid_formatter.input_string == "Hello, World!"

def test_invalid_init(invalid_formatter):
    with pytest.raises(InvalidInputError):
        assert invalid_formatter.input_string  # This should not be reached due to the exception being raised

def test_remove_duplicates():
    formatter = __StringFormatter("hello")
    result = formatter._StringFormatter__remove_duplicates('hheelllloo')
    assert result == 'helo'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0.py:31:13: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_duplicates' member (no-member)

"""