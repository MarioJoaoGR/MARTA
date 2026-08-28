
import pytest
from string_utils.validation import is_url

def test_is_url_basic():
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False
    assert is_url('ftp://files.example.com', allowed_schemes=['ftp']) == True
    assert is_url('http://example.com', allowed_schemes=['https']) == False
    assert is_url('') == False
    assert is_url(None) == False
