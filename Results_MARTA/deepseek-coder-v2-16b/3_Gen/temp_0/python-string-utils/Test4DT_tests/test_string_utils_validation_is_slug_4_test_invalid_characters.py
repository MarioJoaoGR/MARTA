
import re
from unittest.mock import patch
from string_utils.validation import is_full_string, is_slug

def test_invalid_characters():
    # Test cases with invalid characters (uppercase letters and spaces)
    assert not is_slug('My blog post title')  # returns False
    assert not is_slug('my-Blog-post-title')  # returns False
    assert not is_slug('my blog post title')  # returns True
    assert not is_slug('my-blog-post-title ')  # returns False
    assert not is_slug(' my-blog-post-title')  # returns False
