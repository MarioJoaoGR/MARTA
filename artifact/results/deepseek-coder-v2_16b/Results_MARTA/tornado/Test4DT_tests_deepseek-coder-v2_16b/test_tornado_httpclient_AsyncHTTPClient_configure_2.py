
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.mark.asyncio
async def test_valid_input_default_configuration():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert response.body is not None, "Response body should be valid"

@pytest.mark.asyncio
async def test_invalid_force_instance():
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert response.body is not None, "Response body should be valid"

@pytest.mark.asyncio
async def test_configure_with_defaults():
    AsyncHTTPClient.configure(None, defaults=dict(user_agent='MyUserAgent'))
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert response.body is not None, "Response body should be valid"
