# Module: typesystem.fields
# test_typesystem_fields.py
import pytest
from typesystem.fields import String
import re
import typing

# Test 1: Creating a String instance allowing blank values and trimming whitespace
def test_string_creation_allow_blank_and_trim_whitespace():
    str_field = String(allow_blank=True, trim_whitespace=True)
    assert str_field.allow_blank == True
    assert str_field.trim_whitespace == True

# Test 2: Creating a String instance with a maximum length constraint
def test_string_creation_with_max_length():
    str_max_length = String(max_length=10)
    assert str_max_length.max_length == 10

# Test 3: Creating a String instance requiring at least 5 characters and allowing null values
def test_string_creation_min_length_allow_blank():
    str_min_length_allow_null = String(min_length=5, allow_blank=True)
    assert str_min_length_allow_null.min_length == 5
    assert str_min_length_allow_null.allow_blank == True

# Test 4: Creating a String instance with a specific pattern and format
def test_string_creation_with_pattern_and_format():
    str_pattern_format = String(pattern=r"^[a-zA-Z0-9]+$", format="alphanumeric")
    assert isinstance(str_pattern_format.pattern_regex, re.Pattern)
    assert str_pattern_format.format == "alphanumeric"

# Test 5: Creating a String instance with invalid max_length type should raise an assertion error
def test_string_creation_invalid_max_length_type():
    with pytest.raises(AssertionError):
        String(max_length="10")

# Test 6: Creating a String instance with invalid min_length type should raise an assertion error
def test_string_creation_invalid_min_length_type():
    with pytest.raises(AssertionError):
        String(min_length="5")

# Test 7: Creating a String instance with invalid pattern type should raise an assertion error
def test_string_creation_invalid_pattern_type():
    with pytest.raises(AssertionError):
        String(pattern=123)

# Test 8: Creating a String instance with invalid format type should raise an assertion error
def test_string_creation_invalid_format_type():
    with pytest.raises(AssertionError):
        String(format=123)
