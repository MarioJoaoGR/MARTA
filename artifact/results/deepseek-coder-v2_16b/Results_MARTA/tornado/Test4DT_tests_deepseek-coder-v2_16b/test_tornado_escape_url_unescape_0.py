
import pytest
from tornado.escape import url_unescape

def test_url_unescape_default():
    result = url_unescape("https://example.com/?q=hello%20world")
    assert result == 'https://example.com/?q=hello world'

def test_url_unescape_with_encoding_none():
    result = url_unescape(b"https://example.com/?q=hello%20world", encoding=None)
    assert result == b'https://example.com/?q=hello world'

def test_url_unescape_plus_false():
    result = url_unescape("https://example.com/?q=hello+world", plus=False)
    assert result == 'https://example.com/?q=hello+world'

def test_url_unescape_unicode_string():
    result = url_unescape("https://example.com/?q=hello%20world")  # For Unicode string
    assert result == 'https://example.com/?q=hello world'

def test_url_unescape_byte_string():
    result = url_unescape(b"https://example.com/?q=hello%20world", encoding=None)  # For byte string
    assert result == b'https://example.com/?q=hello world'

def test_url_unescape_no_encoded():
    result = url_unescape("https://example.com/")
    assert result == 'https://example.com/'
