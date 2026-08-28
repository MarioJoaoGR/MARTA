
# test_sanic_exceptions_SanicException___init___.py
from sanic import Sanic, request
from sanic.response import json
from sanic.exceptions import SanicException
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("TestApp")
    
    @app.route("/test")
    async def test_route(request):
        raise SanicException("This is a test exception", status_code=404)
    
    return app

@pytest.mark.asyncio
async def test_sanic_exception_with_status_code(app):
    client = await app.asgi_client()
    response = await client.get("/test")
    assert response.status == 404
    data = response.json()
    assert "This is a test exception" in str(data["message"])
    assert data["status"] == 404

@pytest.mark.asyncio
async def test_sanic_exception_default_quiet_true(app):
    client = await app.asgi_client()
    response = await client.get("/test")
    with pytest.raises(SanicException) as exc_info:
        raise SanicException("This is a default quiet exception", status_code=500)
    assert exc_info.value.status_code == 500
    assert exc_info.value.quiet is True
