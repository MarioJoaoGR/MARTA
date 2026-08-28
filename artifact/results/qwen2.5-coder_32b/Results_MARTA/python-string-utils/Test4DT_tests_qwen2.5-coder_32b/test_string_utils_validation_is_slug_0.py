
import re
from string_utils.validation import is_slug

def test_valid_slug():
    assert is_slug('my-blog-post-title') == True

def test_valid_slug_custom_separator():
    assert is_slug('valid_slug', '_') == True

def test_invalid_slug_uppercase():
    assert is_slug('My blog post title') == False

def test_invalid_slug_leading_separator():
    assert is_slug('-invalid-slug') == False

def test_invalid_slug_trailing_separator():
    assert is_slug('invalid-slug-') == False

def test_invalid_slug_special_characters():
    assert is_slug('invalid@slug') == False

def test_non_string_input():
    assert is_slug(12345) == False

def test_none_input():
    assert is_slug(None) == False

def test_empty_string():
    assert is_slug('') == False
