# Module: sanic.exceptions
# test_sanic_exceptions.py
from sanic import Sanic, response
from sanic.exceptions import abort
import pytest

@pytest.fixture
def app():
    return Sanic("MyApp")

def test_abort_with_custom_message(app):
    @app.route("/resource")
    async def get_resource(request):
        abort(404, "Resource not found")
        return response.json({"message": "This should not be reached"})

    with pytest.raises(SanicException) as exc_info:
        app.test_client.get("/resource")
    
    assert str(exc_info.value) == "404: Resource not found"

def test_abort_with_default_message(app):
    @app.route("/resource")
    async def get_resource(request):
        abort(500)
        return response.json({"message": "This should not be reached"})

    with pytest.raises(SanicException) as exc_info:
        app.test_client.get("/resource")
    
    assert str(exc_info.value) == "500: Internal Server Error"

def test_abort_without_message(app):
    @app.route("/resource")
    async def get_resource(request):
        abort(403)
        return response.json({"message": "This should not be reached"})

    with pytest.raises(SanicException) as exc_info:
        app.test_client.get("/resource")
    
    assert str(exc_info.value) == "403: Forbidden"
