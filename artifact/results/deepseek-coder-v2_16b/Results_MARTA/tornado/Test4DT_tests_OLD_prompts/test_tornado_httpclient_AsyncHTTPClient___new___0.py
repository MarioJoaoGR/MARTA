
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient

# Test 1: Basic Usage of AsyncHTTPClient
@pytest.mark.asyncio
async def test_basic_usage():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        instance = mock_client.return_value
        response = MagicMock()
        response.body = b"test body"
        instance.fetch.return_value = response
        
        http_client = AsyncHTTPClient()
        fetched_response = await http_client.fetch("http://www.example.com")
        
        assert fetched_response.body == b"test body"
        mock_client.assert_called_once_with(force_instance=False, **{})

# Test 2: Force Instance Creation
@pytest.mark.asyncio
async def test_force_instance():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        instance = mock_client.return_value
        response = MagicMock()
        response.body = b"test body"
        instance.fetch.return_value = response
        
        http_client = AsyncHTTPClient(force_instance=True)
        fetched_response = await http_client.fetch("http://www.example.com")
        
        assert fetched_response.body == b"test body"
        mock_client.assert_called_once_with(force_instance=True, **{})

# Test 3: Using Defaults
@pytest.mark.asyncio
async def test_using_defaults():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        instance = mock_client.return_value
        response = MagicMock()
        response.body = b"test body"
        instance.fetch.return_value = response
        
        http_client = AsyncHTTPClient(defaults={"user_agent": "MyUserAgent"})
        fetched_response = await http_client.fetch("http://www.example.com")
        
        assert fetched_response.body == b"test body"
        mock_client.assert_called_once_with(force_instance=False, defaults={"user_agent": "MyUserAgent"})

# Test 4: Fetching Data from Google
@pytest.mark.asyncio
async def test_fetching_google():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        instance = mock_client.return_value
        response = MagicMock()
        response.body = b"test body"
        instance.fetch.return_value = response
        
        http_client = AsyncHTTPClient()
        fetched_response = await http_client.fetch("http://www.google.com")
        
        assert fetched_response.body == b"test body"
        mock_client.assert_called_once_with(force_instance=False, **{})

# Test 5: Handling HTTP Errors
@pytest.mark.asyncio
async def test_handling_http_errors():
    with patch('tornado.httpclient.AsyncHTTPClient', autospec=True) as mock_client:
        instance = mock_client.return_value
        with pytest.raises(Exception):
            await instance.fetch("http://www.nonexistentdomain.com")
        
        assert not mock_client.called
