
import pytest
from pytutils.urls import update_query_params

def test_valid_input():
    # Test with valid URL and parameters
    original_url = 'http://example.com?foo=bar&biz=baz'
    updated_params = {'new_param': 'value'}
    expected_url = 'http://example.com?foo=bar&biz=baz&new_param=value'
    
    result = update_query_params(original_url, updated_params)
    assert result == expected_url
