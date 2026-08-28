
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.mark.asyncio
async def test_valid_default_usage():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    print(response.body)

@pytest.mark.asyncio
async def test_force_instance_true():
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    print(response.body)

@pytest.mark.asyncio
async def test_invalid_arguments():
    with pytest.raises(ValueError):
        http_client = AsyncHTTPClient(force_instance=True, defaults=dict(user_agent='MyUserAgent'))
