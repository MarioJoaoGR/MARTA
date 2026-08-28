
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlunsplit, urlencode

def test_valid_input_happy_path():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, params) == expected

def test_valid_input_with_new_param():
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'new_param': 'value'}
    expected = 'http://example.com?foo=bar&biz=baz&new_param=value'
    assert update_query_params(url, params) == expected

