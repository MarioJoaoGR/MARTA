
import pytest
from pytutils.urls import update_query_params

def test_valid_input():
    # Test case with valid URL and parameters
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_output = 'http://example.com?foo=stuff&biz=baz'
    
    assert update_query_params(url, params) == expected_output
