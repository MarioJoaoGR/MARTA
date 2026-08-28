
import pytest
from sanic import Sanic
from sanic.response import stream, StreamingHTTPResponse
import asyncio

# Test scenario 1: Basic streaming function and response
@pytest.mark.asyncio
async def test_stream_basic():
    app = Sanic("MyApp")
    
    @app.route("/")
    async def index(request):
        async def streaming_fn(response):
            await response.write('foo')
            await response.write('bar')
        
        return stream(streaming_fn, content_type='text/plain')
    
    request = app.test_client.get("/")
    assert request.status == 200
    
    body = b""
    async for chunk in request:
        body += chunk
    
    assert body == b'foo' + b'\nbar'

# Test scenario 2: Handling deprecated 'chunked' argument
@pytest.mark.asyncio
async def test_stream_deprecated_chunked():
    app = Sanic("MyApp")
    
    @app.route("/")
    async def index(request):
        async def streaming_fn(response):
            await response.write('foo')
            await response.write('bar')
        
        return stream(streaming_fn, content_type='text/plain', chunked="deprecated")
    
    request = app.test_client.get("/")
    assert request.status == 200
    
    body = b""
    async for chunk in request:
        body += chunk
    
    assert body == b'foo' + b'\nbar'

# Test scenario 3: Custom headers and status code
@pytest.mark.asyncio
async def test_stream_custom_headers():
    app = Sanic("MyApp")
    
    @app.route("/")
    async def index(request):
        async def streaming_fn(response):
            await response.write('foo')
            await response.write('bar')
        
        return stream(streaming_fn, status=201, headers={"X-Custom": "Value"})
    
    request = app.test_client.get("/")
    assert request.status == 201
    assert request.headers["X-Custom"] == "Value"
    
    body = b""
    async for chunk in request:
        body += chunk
    
    assert body == b'foo' + b'\nbar'
