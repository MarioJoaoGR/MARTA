
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse

# Test 1: Basic Usage of AsyncHTTPClient
@pytest.mark.asyncio
async def test_basic_usage():
    with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch = MagicMock(return_value=HTTPResponse())
        
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://www.google.com")
        
        assert isinstance(response, HTTPResponse)
        mock_instance.fetch.assert_called_once_with("http://www.google.com")

# Test 2: Fetching with Defaults
@pytest.mark.asyncio
async def test_fetch_with_defaults():
    with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.configure = MagicMock()
        mock_instance.configure.return_value = None
        
        http_client = AsyncHTTPClient()
        defaults = {"user_agent": "MyUserAgent"}
        AsyncHTTPClient.configure(None, defaults=defaults)
        response = await http_client.fetch("http://www.google.com")
        
        assert isinstance(response, HTTPResponse)
        mock_instance.configure.assert_called_once_with(None, defaults=defaults)

# Test 3: Force Instance Creation
@pytest.mark.asyncio
async def test_force_instance():
    with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch = MagicMock(return_value=HTTPResponse())
        
        http_client = AsyncHTTPClient(force_instance=True)
        response = await http_client.fetch("http://www.google.com")
        
        assert isinstance(response, HTTPResponse)
        mock_instance.fetch.assert_called_once_with("http://www.google.com")

# Test 4: Fetching with Custom Headers
@pytest.mark.asyncio
async def test_fetch_with_headers():
    with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch = MagicMock(return_value=HTTPResponse())
        
        request = {"url": "http://www.google.com", "headers": {"User-Agent": "MyCustomUserAgent"}}
        response = await mock_instance.fetch(request)
        
        assert isinstance(response, HTTPResponse)
        mock_instance.fetch.assert_called_once_with(request)

# Test 5: Handling HTTP Errors
@pytest.mark.asyncio
async def test_handle_errors():
    with patch('tornado.httpclient.AsyncHTTPClient') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.fetch = MagicMock(side_effect=Exception("Error"))
        
        http_client = AsyncHTTPClient()
        with pytest.raises(Exception):
            await http_client.fetch("http://www.nonexistentdomain.com")
        
        assert mock_instance.fetch.call_count == 1
