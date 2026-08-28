
# Module: typesystem.fields
# test_typesystem_fields.py
import pytest
from typesystem.fields import String
import re
import typing

# Test 9: Creating a String instance with pattern directly assigned as a regex object
def test_string_creation_with_pattern_as_regex():
    pattern = re.compile(r"^[a-zA-Z0-9]+$")
    str_field = String(pattern=pattern)
    assert isinstance(str_field.pattern_regex, re.Pattern)
    assert str_field.pattern == pattern.pattern

# Test 10: Creating a String instance with invalid max_length value should raise an assertion error
def test_string_creation_invalid_max_length_value():
    with pytest.raises(AssertionError):
        String(max_length="ten")

# Test 11: Creating a String instance with invalid min_length value should raise an assertion error
def test_string_creation_invalid_min_length_value():
    with pytest.raises(AssertionError):
        String(min_length="five")

# Test 12: Creating a String instance with invalid pattern value should raise an assertion error
def test_string_creation_invalid_pattern_value():
    with pytest.raises(AssertionError):
        String(pattern=123)

# Test 13: Creating a String instance with invalid format value should raise an assertion error
def test_string_creation_invalid_format_value():
    with pytest.raises(AssertionError):
        String(format=123)
