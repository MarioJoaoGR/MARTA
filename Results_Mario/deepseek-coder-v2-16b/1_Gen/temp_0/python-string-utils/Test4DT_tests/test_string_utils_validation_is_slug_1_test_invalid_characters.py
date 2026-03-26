
import re
from string_utils.validation import is_full_string, is_slug

def test_invalid_characters():
    input_string = 'My blog post title'
    assert not is_slug(input_string), "Expected False for invalid slug with uppercase letters and spaces"
