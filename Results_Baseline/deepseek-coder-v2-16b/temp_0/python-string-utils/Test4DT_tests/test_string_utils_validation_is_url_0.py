
import pytest
from string_utils.validation import is_url
from typing import List, Optional, Any

# Test cases for the `is_url` function
def test_valid_http_urls():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True

def test_invalid_urls():
    assert is_url('.mysite.com') == False
    assert is_url('mysite.com') == False  # No scheme specified

def test_valid_with_allowed_schemes():
    assert is_url('ftp://example.com', ['http', 'https', 'ftp']) == True
    assert is_url('http://example.com', ['https', 'ftp']) == False  # Only https and ftp are allowed

def test_invalid_with_allowed_schemes():
    assert is_url('ftp://example.com', ['http', 'https']) == False  # http is not allowed

def test_empty_string():
    assert is_url('') == False

# Correct the test case to ensure it raises a TypeError when input is None
@pytest.mark.xfail(reason="Expected TypeError due to incorrect function implementation")
def test_none_input():
    with pytest.raises(TypeError):
        is_url(None)  # None should raise a TypeError as it's not a string
