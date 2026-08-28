# Module: string_utils.validation
import pytest
from string_utils.validation import is_slug


def test_is_slug_valid_default_separator():
    assert is_slug('my-blog-post-title') == True

def test_is_slug_invalid_due_to_uppercase_and_spaces():
    assert is_slug('My blog post title') == False

def test_is_slug_valid_with_custom_separator():
    assert is_slug('valid_slug', '_') == True

def test_is_slug_empty_string():
    assert is_slug('') == False

def test_is_slug_numeric_only_string():
    assert is_slug('123456') == True

def test_is_slug_multiple_separators():
    assert is_slug('multiple---separators') == True

def test_is_slug_invalid_with_special_characters():
    assert is_slug('invalid@slug#with$special%chars') == False

def test_is_slug_valid_with_numbers_and_default_separator():
    assert is_slug('number123-in-slug') == True

def test_is_slug_invalid_starting_with_separator():
    assert is_slug('-invalid-start') == False

def test_is_slug_invalid_ending_with_separator():
    assert is_slug('invalid-end-') == False

def test_is_slug_valid_single_character():
    assert is_slug('a') == True

def test_is_slug_valid_single_number():
    assert is_slug('1') == True
