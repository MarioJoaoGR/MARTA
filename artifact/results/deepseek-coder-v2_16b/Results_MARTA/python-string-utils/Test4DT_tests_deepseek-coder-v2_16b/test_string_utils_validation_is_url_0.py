
import pytest
from string_utils.validation import is_url

def test_is_url_with_allowed_schemes():
    allowed_schemes = ['http', 'https']
    assert is_url('http://www.mysite.com', allowed_schemes) == True
    assert is_url('https://mysite.com', allowed_schemes) == True
    assert is_url('ftp://mysite.com', allowed_schemes) == False


def test_is_url_invalid_scheme():
    assert is_url('http://www.mysite.com', allowed_schemes=['https']) == False