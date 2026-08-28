
import pytest
from tornado.httpclient import AsyncHTTPClient


def test_invalid_argument():
    # Test that an invalid argument raises a NotImplementedError
    with pytest.raises(TypeError):
        AsyncHTTPClient.configure(foo='bar')