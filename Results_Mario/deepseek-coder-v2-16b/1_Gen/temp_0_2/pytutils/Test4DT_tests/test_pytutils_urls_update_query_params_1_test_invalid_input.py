
import pytest
from pytutils.urls import update_query_params

def test_invalid_input():
    with pytest.raises(TypeError):
        update_query_params('http://example.com?foo=bar&biz=baz', 'invalid_params')
