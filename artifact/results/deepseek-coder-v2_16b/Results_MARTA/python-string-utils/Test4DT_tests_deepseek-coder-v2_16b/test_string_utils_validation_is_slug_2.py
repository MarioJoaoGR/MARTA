
import re
from typing import Any
import pytest

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string) > 0

def is_slug(input_string: Any, separator: str = '-') -> bool:
    """
    Checks if a given string is a slug (as created by `slugify()`).

    *Examples:*

    >>> is_slug('my-blog-post-title') # returns true
    >>> is_slug('My blog post title') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param separator: Join sign used by the slug.
    :type separator: str
    :return: True if slug, false otherwise.
    """
    if not is_full_string(input_string):
        return False

    rex = r'^([a-z\d]+' + re.escape(separator) + r'*?)*[a-z\d]$'

    return re.match(rex, input_string) is not None

# Test cases for valid slug
def test_valid_slug():
    assert is_slug('my-blog-post-title') == True

# Test cases for invalid characters in slug (uppercase letters, spaces)
def test_invalid_characters():
    assert is_slug('My blog post title') == False

# Test cases for empty string input
def test_empty_string():
    assert is_slug('') == False
