
import pytest
from string_utils.validation import is_camel_case

@pytest.mark.parametrize("input_string, expected", [
    (None, False),
    ("", False),
    ("1MyString", False),
    ("myString", True),
    ("MyString", True),
    ("my2String", False),  # Contains a number after the first letter
    ("MYSTRING", False),   # All uppercase is not camel case
    ("my_string", False),  # Contains underscore, not camel case
])
def test_edge_cases(input_string, expected):
    assert is_camel_case(input_string) == expected
