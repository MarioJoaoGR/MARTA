
import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse, HTTPError
import asyncio

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def http_client():
    return AsyncHTTPClient()

# Test fetching a valid HTTP request
@pytest.mark.asyncio
async def test_valid_fetch_request(http_client):
    response = await http_client.fetch("http://www.google.com")
    assert response.code == 200, f"Expected status code 200, got {response.code}"
    assert "Google" in str(response.body), "Response body does not contain 'Google'"

# Test raising ValueError when providing invalid arguments to fetch
@pytest.mark.asyncio
async def test_invalid_fetch_request():
    http_client = AsyncHTTPClient()
    with pytest.raises(ValueError):
        await http_client.fetch("http://www.google.com", headers={})

# Test error handling for non-200 response codes
@pytest.mark.asyncio
async def test_error_handling(http_client):
    with pytest.raises(HTTPError) as excinfo:
        await http_client.fetch("http://www.invalidurl.com", raise_error=False)
    assert isinstance(excinfo.value, HTTPError), "Expected an HTTPError"
    assert excinfo.value.code != 200, f"Expected non-200 status code, got {excinfo.value.code}"
