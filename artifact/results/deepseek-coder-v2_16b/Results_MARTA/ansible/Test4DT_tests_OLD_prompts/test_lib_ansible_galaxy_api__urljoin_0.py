
import pytest
from ansible.galaxy.api import urljoin as _urljoin_func


def test_urljoin_multiple_slashes():
    with pytest.raises(TypeError):
        _urljoin_func('https://example.org/', '/path/', 'to', 'resource')

def test_urljoin_empty_string():
    with pytest.raises(TypeError):
        _urljoin_func('ftp://server/', '', 'files/', 'readme.txt')

def test_urljoin_whitespace():
    with pytest.raises(TypeError):
        _urljoin_func('http://example.com', ' ', 'subdomain', ' ')