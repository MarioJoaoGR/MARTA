# Module: string_utils.validation
import pytest
from string_utils.validation import is_url
from typing import List, Optional

# Test cases for the is_url function
def test_valid_http_url():
    assert is_url('http://www.mysite.com') == True

def test_valid_https_url():
    assert is_url('https://mysite.com', allowed_schemes=['https']) == True

def test_invalid_url():
    assert is_url('.mysite.com') == False

def test_valid_ftp_url():
    assert is_url('ftp://example.com', allowed_schemes=['http', 'https', 'ftp']) == True

def test_invalid_scheme_without_allowed_schemes():
    assert is_url('file:///local/path') == False

def test_valid_default_scheme():
    assert is_url('http://www.example.com', allowed_schemes=None) == True

# Additional edge cases and invalid inputs can be added to ensure robustness
