
import pytest
from sanic import Sanic
from sanic.response import text

@pytest.fixture(scope="module")
def app():
    app = Sanic("TestApp")
    
    @app.route("/test")
    async def test_endpoint(request):
        return text("Hello, world!")
    
    return app

@pytest.mark.asyncio
async def test_sanic_headers_options_0(app):
    client = app.test_client

    response = await client().options("http://example.com/test", headers={"x-scheme": "https"})
    
    assert response.status == 200
    assert response.method == "OPTIONS"
    assert response.headers["allow"] == "OPTIONS, GET, POST, PUT, PATCH, DELETE, HEAD"
