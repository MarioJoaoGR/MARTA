
import pytest
from string_utils.validation import is_url
from typing import List, Optional

# Test cases for the `is_url` function
def test_valid_http_url():
    assert is_url('http://www.mysite.com') == True

def test_valid_https_url():
    assert is_url('https://mysite.com') == True

def test_invalid_url():
    assert is_url('.mysite.com') == False

def test_valid_with_allowed_schemes():
    allowed_schemes = ['http', 'https']
    assert is_url('http://www.mysite.com', allowed_schemes) == True

def test_invalid_with_allowed_schemes():
    allowed_schemes = ['http', 'https']
    assert is_url('ftp://mysite.com', allowed_schemes) == False

# Additional edge cases can be added to cover more scenarios
