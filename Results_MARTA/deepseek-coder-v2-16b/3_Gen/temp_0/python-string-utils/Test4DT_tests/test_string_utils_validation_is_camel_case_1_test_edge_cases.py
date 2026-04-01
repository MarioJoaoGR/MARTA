
import pytest
from string_utils.validation import is_camel_case

@pytest.mark.parametrize("input_string, expected", [
    (None, False),
    ("", False),
    ("1MyString", False),
    ("myString", True),
    ("MyString", True),
])
def test_edge_cases(input_string, expected):
    assert is_camel_case(input_string) == expected
