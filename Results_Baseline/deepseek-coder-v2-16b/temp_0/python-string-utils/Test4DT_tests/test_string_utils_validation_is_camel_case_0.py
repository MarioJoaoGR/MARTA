
import pytest
from string_utils.validation import is_camel_case

# Test cases for the is_camel_case function
def test_is_camel_case_true():
    assert is_camel_case('myString') == True
    assert is_camel_case('MyString') == True