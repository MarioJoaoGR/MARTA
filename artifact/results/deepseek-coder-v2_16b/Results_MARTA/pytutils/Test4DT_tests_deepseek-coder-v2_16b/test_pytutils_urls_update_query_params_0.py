
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlunsplit, urlencode

def test_update_query_params_with_valid_input():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    result = update_query_params(url, params)
    assert result == expected_url

def test_update_query_params_with_new_param():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'new_param': 'value'}
    expected_url = 'http://example.com?foo=bar&biz=baz&new_param=value'
    result = update_query_params(url, params)
    assert result == expected_url

