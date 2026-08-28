
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.mark.asyncio
async def test_valid_instance():
    http_client = AsyncHTTPClient()
    assert isinstance(http_client, AsyncHTTPClient)

@pytest.mark.asyncio
async def test_invalid_argument():
    with pytest.raises(TypeError):
        AsyncHTTPClient(force_new_instance=True)
