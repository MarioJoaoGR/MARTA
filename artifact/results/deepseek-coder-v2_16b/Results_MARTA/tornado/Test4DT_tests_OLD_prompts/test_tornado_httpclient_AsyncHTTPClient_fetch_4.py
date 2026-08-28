
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse, HTTPError

# Test scenarios
@pytest.mark.asyncio
async def test_valid_input():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch.return_value = MagicMock(spec=HTTPResponse, status_code=200)
        
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://www.google.com")
        
        assert isinstance(response, HTTPResponse)
        mock_instance.fetch.assert_called_once_with(HTTPRequest("http://www.google.com"))

@pytest.mark.asyncio
async def test_none_input():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        http_client = AsyncHTTPClient()
        with pytest.raises(TypeError):
            await http_client.fetch(None)

@pytest.mark.asyncio
async def test_invalid_input():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        http_client = AsyncHTTPClient()
        with pytest.raises(ValueError):
            await http_client.fetch(12345)
