
import pytest
from urllib.parse import urlparse

def get_cache_id(url):
    """ Gets the cache ID for the URL specified. """
    url_info = urlparse(url)

    port = None
    try:
        port = url_info.port
    except ValueError:
        pass  # While the URL is probably invalid, let the caller figure that out when using it

    # Cannot use netloc because it could contain credentials if the server specified had them in there.
    return '%s:%s' % (url_info.hostname, port or '')

# Test cases
def test_valid_input():
    url = 'http://example.com/path?query=1#fragment'
    assert get_cache_id(url) == 'example.com:'

def test_edge_case_none():
    url = None
    with pytest.raises(TypeError):
        get_cache_id(url)

def test_invalid_input():
    url = 'invalid-url'
    with pytest.raises(ValueError):
        get_cache_id(url)
