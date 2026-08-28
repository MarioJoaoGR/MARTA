# Module: tornado.httpclient
# test_tornado_httpclient.py
import pytest
from tornado.httpclient import AsyncHTTPClient
from typing import Dict, Optional
import weakref

class IOLoop:
    pass

@pytest.fixture(scope="module")
def http_client():
    return AsyncHTTPClient()

@pytest.mark.asyncio
async def test_default_initialization(http_client):
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"

@pytest.mark.asyncio
async def test_forced_instance():
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"

@pytest.mark.asyncio
async def test_with_defaults():
    AsyncHTTPClient.configure(None, defaults={"user_agent": "MyUserAgent"})
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"
    assert response.headers['User-Agent'] == "MyUserAgent", "User-Agent header should match the default value"

@pytest.mark.asyncio
async def test_with_force_instance_and_defaults():
    AsyncHTTPClient.configure(None, defaults={"user_agent": "MyUserAgent"})
    http_client = AsyncHTTPClient(force_instance=True)
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"
    assert response.headers['User-Agent'] == "MyUserAgent", "User-Agent header should match the default value"

@pytest.mark.asyncio
async def test_using_specific_implementation():
    from tornado.curl_httpclient import CurlAsyncHTTPClient
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"

@pytest.mark.asyncio
async def test_initialization_with_max_clients():
    AsyncHTTPClient.configure(None, max_clients=20)
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("http://www.google.com")
    assert response is not None, "Response should be non-None"
    assert hasattr(response, 'body'), "Response should have a body attribute"
