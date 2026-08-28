
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture(scope="module")
def http_client():
    client = AsyncHTTPClient()
    yield client
    client.close()

@pytest.mark.asyncio
async def test_fetch_google_com(http_client):
    response = await http_client.fetch("http://www.google.com")
    assert response is not None
    assert response.body is not None
    print(response.body)
