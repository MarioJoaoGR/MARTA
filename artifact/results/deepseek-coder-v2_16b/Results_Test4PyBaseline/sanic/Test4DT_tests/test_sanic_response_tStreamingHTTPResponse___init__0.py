# Module: sanic.response
import pytest
from starlette.responses import StreamingHTTPResponse
import asyncio

# Test cases for the deprecated `StreamingHTTPResponse` class

def test_basic_usage():
    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(1)
        await response.write("bar")
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test():
        response = StreamingHTTPResponse(sample_streaming_fn)
        assert response.status == 200
        assert response.content_type == "text/plain; charset=utf-8"
    
    test()

def test_custom_status_and_headers():
    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(1)
        await response.write("bar")
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test():
        response = StreamingHTTPResponse(sample_streaming_fn, status=201, headers={"X-Custom-Header": "Value"})
        assert response.status == 201
        assert response.headers["X-Custom-Header"] == "Value"
    
    test()

def test_custom_content_type():
    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(1)
        await response.write("bar")
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test():
        response = StreamingHTTPResponse(sample_streaming_fn, content_type="application/json")
        assert response.content_type == "application/json"
    
    test()

def test_handling_deprecated_arguments():
    async def sample_streaming_fn(response):
        await response.write("foo")
        await asyncio.sleep(1)
        await response.write("bar")
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test():
        with pytest.warns(DeprecationWarning):
            response = StreamingHTTPResponse(sample_streaming_fn, chunked="not applicable")
    
    test()
