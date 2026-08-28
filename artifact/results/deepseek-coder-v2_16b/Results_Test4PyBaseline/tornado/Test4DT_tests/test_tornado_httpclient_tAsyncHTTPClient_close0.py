
import pytest
from tornado.httpclient import AsyncHTTPClient

# Test cases for AsyncHTTPClient class
def test_default_instantiation():
    http_client = AsyncHTTPClient()
    assert isinstance(http_client, AsyncHTTPClient), "Instance should be of type AsyncHTTPClient"

def test_configure_defaults():
    AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
    client = AsyncHTTPClient()
    assert hasattr(client, 'defaults'), "Client should have a 'defaults' attribute after configuration"