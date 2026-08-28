
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse, HTTPError

# Test scenarios
@pytest.mark.asyncio
async def test_valid_input():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch.return_value = MagicMock(spec=HTTPResponse, body="mocked response")
        
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://www.google.com")
        
        assert isinstance(response, HTTPResponse)
        assert response.body == "mocked response"
        mock_instance.fetch.assert_called_once_with("http://www.google.com", raise_error=True)

@pytest.mark.asyncio
async def test_edge_case():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch.side_effect = HTTPError(error="mocked error")
        
        http_client = AsyncHTTPClient()
        with pytest.raises(HTTPError):
            await http_client.fetch(None)
        
        assert mock_instance.fetch.call_count == 1
        mock_instance.fetch.assert_called_once_with(None, raise_error=True)

@pytest.mark.asyncio
async def test_invalid_input():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        http_client = AsyncHTTPClient()
        with pytest.raises(ValueError):
            await http_client.fetch(12345)
        
        assert not mock_client.return_value.fetch.called
