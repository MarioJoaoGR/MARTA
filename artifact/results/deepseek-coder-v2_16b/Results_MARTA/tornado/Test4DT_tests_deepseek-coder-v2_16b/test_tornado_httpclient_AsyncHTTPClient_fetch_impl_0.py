
import pytest
from tornado.httpclient import AsyncHTTPClient

class TestAsyncHTTPClient:
    
    @pytest.mark.asyncio
    async def test_basic_usage(self):
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch("http://www.google.com")
            assert isinstance(response, HTTPResponse)
            assert "Google" in str(response.body)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")
    
    @pytest.mark.asyncio
    async def test_fetch_with_defaults(self):
        http_client = AsyncHTTPClient()
        defaults = {"user_agent": "MyUserAgent"}
        AsyncHTTPClient.configure(None, defaults=defaults)
        try:
            response = await http_client.fetch("http://www.google.com")
            assert isinstance(response, HTTPResponse)
            assert "Google" in str(response.body)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")
    
    @pytest.mark.asyncio
    async def test_force_instance(self):
        http_client = AsyncHTTPClient(force_instance=True)
        try:
            response = await http_client.fetch("http://www.google.com")
            assert isinstance(response, HTTPResponse)
            assert "Google" in str(response.body)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")
    
    @pytest.mark.asyncio
    async def test_fetch_with_headers(self):
        http_client = AsyncHTTPClient()
        request = {"url": "http://www.google.com", "headers": {"User-Agent": "MyCustomUserAgent"}}
        try:
            response = await http_client.fetch(request)
            assert isinstance(response, HTTPResponse)
            assert "Google" in str(response.body)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")
    
    @pytest.mark.asyncio
    async def test_handle_errors(self):
        http_client = AsyncHTTPClient()
        try:
            with pytest.raises(Exception) as excinfo:
                await http_client.fetch("http://www.nonexistentdomain.com")
            assert "Unknown scheme" in str(excinfo.value)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")
