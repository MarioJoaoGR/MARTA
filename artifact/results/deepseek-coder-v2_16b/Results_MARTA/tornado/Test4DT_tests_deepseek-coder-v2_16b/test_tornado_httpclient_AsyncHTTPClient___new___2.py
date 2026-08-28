
import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse

class TestAsyncHTTPClient:
    @pytest.mark.asyncio
    async def test_basic_usage(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://www.example.com")
        assert response.code == 200, f"Expected status code 200, but got {response.code}"
        assert "Example Domain" in str(response.body), "Response body does not contain 'Example Domain'"

    @pytest.mark.asyncio
    async def test_force_instance(self):
        http_client1 = AsyncHTTPClient(force_instance=True)
        response1 = await http_client1.fetch("http://www.example.com")
        
        http_client2 = AsyncHTTPClient(force_instance=True)
        response2 = await http_client2.fetch("http://www.example.com")
        
        assert id(http_client1) != id(http_client2), "Expected different instances due to force_instance"
        assert response1.body == response2.body, "Expected same body for different instances with force_instance"

    @pytest.mark.asyncio
    async def test_invalid_inputs(self):
        http_client = AsyncHTTPClient()
        with pytest.raises(RuntimeError):
            await http_client.fetch("http://example.com", force_instance=True, invalid_arg="invalid")

    @pytest.mark.asyncio
    async def test_defaults(self):
        http_client = AsyncHTTPClient(defaults={"user_agent": "MyUserAgent"})
        response = await http_client.fetch("http://www.example.com")
        assert "MyUserAgent" in response.headers["User-Agent"], "Expected custom user agent to be set"
