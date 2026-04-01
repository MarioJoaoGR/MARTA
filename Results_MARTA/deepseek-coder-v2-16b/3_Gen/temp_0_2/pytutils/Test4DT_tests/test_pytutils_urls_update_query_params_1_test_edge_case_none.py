
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlencode, urlsplit, urlunsplit

def test_edge_case_none():
    with pytest.raises(TypeError):
        update_query_params('http://example.com?foo=bar&biz=baz', None)
