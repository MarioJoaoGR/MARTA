
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.mark.asyncio
async def test_valid_case():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert len(response.body) > 0, "Response body should contain data"

@pytest.mark.asyncio
async def test_force_instance():
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert len(response.body) > 0, "Response body should contain data"

@pytest.mark.asyncio
async def test_configure_defaults():
    AsyncHTTPClient.configure(None, defaults=dict(user_agent='MyUserAgent'))
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert len(response.body) > 0, "Response body should contain data"
    assert http_client._defaults['user_agent'] == 'MyUserAgent', "User agent should be configured correctly"
