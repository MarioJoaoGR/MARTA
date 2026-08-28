# Module: tornado.simple_httpclient
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

@pytest.fixture
def simple_http_client():
    return SimpleAsyncHTTPClient()

@patch('tornado.simple_httpclient._HTTPConnection')
def test_connection_class(mock_http_connection, simple_http_client):
    assert simple_http_client._connection_class() == mock_http_connection

@pytest.mark.asyncio
async def test_fetch():
    with patch('tornado.simple_httpclient._HTTPConnection') as mock_http_connection:
        mock_response = MagicMock()
        mock_response.body = b"Test Body"
        mock_http_connection.return_value.fetch.return_value = mock_response
        
        simple_http_client = SimpleAsyncHTTPClient()
        response = await simple_http_client.fetch("http://www.google.com")
        
        assert response.body == b"Test Body"
