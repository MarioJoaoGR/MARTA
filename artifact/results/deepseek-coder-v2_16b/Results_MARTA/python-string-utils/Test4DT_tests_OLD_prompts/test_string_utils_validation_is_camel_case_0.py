
import pytest
from string_utils.validation import is_camel_case

# Test valid camel case input
def test_valid_camel_case():
    assert is_camel_case('myString') == True

# Test invalid camel case input with mixed casing but not starting with a lowercase letter

# Test invalid camel case input with numbers at the beginning
def test_invalid_numbers_at_beginning():
    assert not is_camel_case('123myString')

# Test invalid camel case input with only lowercase letters
def test_invalid_only_lowercase():
    assert not is_camel_case('onlylowercaseletters')

# Test invalid camel case input with empty string
def test_invalid_empty_string():
    assert not is_camel_case('')