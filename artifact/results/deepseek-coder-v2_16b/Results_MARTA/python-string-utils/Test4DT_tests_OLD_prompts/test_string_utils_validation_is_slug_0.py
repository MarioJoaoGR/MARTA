
import pytest
from unittest.mock import patch
from string_utils.validation import is_slug

# Test valid slug input
def test_valid_slug():
    with patch('string_utils.validation.is_full_string', return_value=True):
        assert is_slug('my-blog-post-title') == True

# Test invalid characters (uppercase letters and spaces)
def test_invalid_characters():
    with patch('string_utils.validation.is_full_string', return_value=True):
        assert is_slug('My blog post title') == False

# Test empty string input
def test_empty_string():
    with patch('string_utils.validation.is_full_string', return_value=False):
        assert is_slug('') == False
