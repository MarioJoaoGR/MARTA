
import re
from string_utils.validation import is_slug

def test_none_input():
    assert not is_slug(None)  # This should return False as None does not match the slug pattern
