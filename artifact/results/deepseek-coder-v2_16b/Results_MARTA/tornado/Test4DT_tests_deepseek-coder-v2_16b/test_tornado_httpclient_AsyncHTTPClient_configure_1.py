
import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.mark.asyncio
async def test_valid_inputs():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be valid"
    assert hasattr(response, 'body'), "Response should have a body attribute"

@pytest.mark.asyncio
async def test_edge_cases():
    with pytest.raises(Exception):
        AsyncHTTPClient.configure(None)
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.example.com")
    assert response is None, "Response should be None for invalid inputs"

@pytest.mark.asyncio
async def test_invalid_inputs():
    with pytest.raises(Exception):
        AsyncHTTPClient()
