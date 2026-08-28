
import pytest
from string_utils.validation import is_url
from unittest.mock import patch

# Test valid URL input with default behavior (any scheme allowed)
def test_valid_url():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True

# Test invalid URL input
def test_invalid_url():
    assert is_url('.mysite.com') == False

# Test valid URL with specified allowed schemes
def test_valid_url_with_allowed_schemes():
    allowed_schemes = ['http', 'https']
    assert is_url('http://www.mysite.com', allowed_schemes) == True
    assert is_url('https://mysite.com', allowed_schemes) == True
    assert is_url('ftp://mysite.com', allowed_schemes) == False

# Test invalid input type, should raise TypeError

# Test empty string, should return False
def test_empty_string():
    assert is_url('') == False