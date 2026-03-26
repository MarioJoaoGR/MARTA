
# Module: string_utils.manipulation
# test_string_utils.py
from string_utils.manipulation import __StringFormatter
import pytest

def is_string(input_value):
    return isinstance(input_value, str)

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

def test_uppercase_first_char():
    formatter = __StringFormatter("hello world")
    assert formatter._StringFormatter__uppercase_first_char() == "Hello World"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:31:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__uppercase_first_char' member (no-member)

"""