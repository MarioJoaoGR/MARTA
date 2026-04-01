
import pytest
from pytutils.urls import update_query_params

def test_edge_case_none():
    url = "http://example.com?foo=bar&biz=baz"
    params = {}
    expected_url = "http://example.com?foo=bar&biz=baz"
    
    result = update_query_params(url, params)
    
    assert result == expected_url
