
import re
from string_utils.validation import is_slug

def test_valid_slug():
    input_string = 'my-blog-post-title'
    assert is_slug(input_string) == True
