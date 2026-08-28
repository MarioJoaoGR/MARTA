
import pytest
from sanic import Sanic
from sanic.response import stream, text
import asyncio

# Define a sample streaming function for testing
async def sample_streaming_fn(response):
    await response.write('foo')
    await asyncio.sleep(0.1)  # Simulate some processing time
    await response.write('bar')

# Create the Sanic app instance
@pytest.fixture
def app():
    return Sanic("MyApp")

# Define a route that uses the stream function for testing
@pytest.mark.asyncio
@pytest.mark.parametrize("content_type", ["text/event-stream"])
async def test_sanic_response_stream(app, content_type):
    @app.route("/")
    async def index(request):
        return stream(sample_streaming_fn, content_type=content_type)

    # Create a client to simulate a request to the app
    request, response = await app.asgi_client.get("/", headers={"accept": content_type})

    # Assert that the response status code is 200
    assert response.status == 200

    # Read and check the streamed content
    body = b""
    async for chunk in response.stream:
        body += chunk
    assert body == b'foo' + b'bar'
