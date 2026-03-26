
import re
from string_utils.manipulation import strip_html, InvalidInputError
import pytest

def is_string(input_str):
    return isinstance(input_str, str)

HTML_TAG_ONLY_RE = re.compile(r'<[^>]+>', re.IGNORECASE)
HTML_RE = re.compile(r'<!--.*?-->|<\w+\b[^>]*>.*?</\w+>|<[^>]+>', re.IGNORECASE)

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_html(12345)  # Non-string input
