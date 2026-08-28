
import pytest
from tornado import escape
from unittest.mock import patch

def url_unescape(value, encoding="utf-8", plus=True):
    if isinstance(value, bytes):
        value = value.decode(encoding)
    if plus:
        return escape.url_unescape(value)
    else:
        # Replace '+' with space manually for the test case where it should not be unescaped
        return value.replace('+', ' ')

@pytest.mark.parametrize("input_value, expected", [
    ("https://example.com/search?q=hello+world", "https://example.com/search?q=hello world"),
    (b"https://example.com/search?q=hello%20world", "https://example.com/search?q=hello world")
])
def test_url_unescape(input_value, expected):
    assert url_unescape(input_value) == expected

@pytest.mark.parametrize("input_value, encoding, expected", [
    ("https://example.com/search?q=hello+world", "latin1", "https://example.com/search?q=hello world"),
    (b"https://example.com/search?q=hello%20world", "latin1", "https://example.com/search?q=hello world")
])
def test_url_unescape_with_encoding(input_value, encoding, expected):
    assert url_unescape(input_value, encoding) == expected
