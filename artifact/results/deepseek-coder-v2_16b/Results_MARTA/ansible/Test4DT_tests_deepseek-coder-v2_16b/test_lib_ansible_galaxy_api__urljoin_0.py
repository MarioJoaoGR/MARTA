
import pytest
from ansible.galaxy.api import _urljoin

def test_urljoin_basic():
    joined_url = _urljoin('http://example.com', 'subdomain', 'page')
    assert joined_url == 'http://example.com/subdomain/page'

def test_urljoin_multiple_slashes():
    joined_url = _urljoin('https://example.org/', '/path/', 'to', 'resource')
    assert joined_url == 'https://example.org/path/to/resource'

def test_urljoin_empty_string():
    joined_url = _urljoin('ftp://server/', '', 'files/', 'readme.txt')
    assert joined_url == 'ftp://server/files/readme.txt'
