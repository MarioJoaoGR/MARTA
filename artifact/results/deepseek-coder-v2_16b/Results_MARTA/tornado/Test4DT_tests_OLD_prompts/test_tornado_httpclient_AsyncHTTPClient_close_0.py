
import pytest
from tornado.httpclient import AsyncHTTPClient
import asyncio

@pytest.mark.asyncio
async def test_fetch_google():
    http_client = AsyncHTTPClient()
    with pytest.raises(Exception) as excinfo:
        response = await http_client.fetch('http://www.google.com')
    assert str(excinfo.value) == "HTTP 403 Forbidden"

@pytest.mark.asyncio
async def test_force_instance():
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch('http://www.google.com')
    assert response.code == 200

@pytest.mark.asyncio
async def test_configure_defaults():
    AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
    http_client = AsyncHTTPClient()
    response = await http_client.fetch('http://www.google.com')
    assert response.code == 200

@pytest.mark.asyncio
async def test_close():
    http_client = AsyncHTTPClient(force_instance=True)
    http_client.close()
    with pytest.raises(RuntimeError):
        await http_client.fetch('http://www.google.com')
