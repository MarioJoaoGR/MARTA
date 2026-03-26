
import pytest
from string_utils.validation import is_camel_case

@pytest.mark.parametrize("test_input, expected", [
    (None, False),
    ("", False),
    ("1MyString", False),
    ("myString", True),
    ("MyString", True),
])
def test_is_camel_case(test_input, expected):
    assert is_camel_case(test_input) == expected
