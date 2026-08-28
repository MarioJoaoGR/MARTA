
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient

def test_configure():
    with patch('tornado.httpclient.AsyncHTTPClient._instance_cache', None):
        AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
        client = AsyncHTTPClient()
        assert client.defaults['user_agent'] == "MyUserAgent", "Expected default user agent to be set."
