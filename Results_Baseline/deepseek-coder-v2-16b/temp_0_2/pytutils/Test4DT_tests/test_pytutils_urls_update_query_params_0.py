
import pytest
from urllib.parse import urlparse, parse_qs, urlunsplit, urlencode
from pytutils.urls import update_query_params

# Test cases for the update_query_params function

def test_update_basic():
    """Test updating a single parameter in the URL."""
    assert update_query_params('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}) == 'http://example.com?foo=stuff&biz=baz'

def test_update_multiple_params():
    """Test adding multiple parameters to the URL."""