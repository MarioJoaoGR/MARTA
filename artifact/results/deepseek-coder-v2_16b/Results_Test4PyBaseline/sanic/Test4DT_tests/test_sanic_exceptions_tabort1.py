
# Module: sanic.exceptions
# test_sanic_exceptions.py
from sanic import Sanic, response
from sanic.exceptions import abort, STATUS_CODES, SanicException
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

# New test cases to cover uncovered lines 245 and 247
def test_abort_with_none_message():
    with pytest.raises(SanicException):
        abort(400)  # Assuming 400 has a default message defined in STATUS_CODES

def test_abort_with_non_string_non_bytes_message():
    with pytest.raises(TypeError):
        abort(400, None)  # Providing a non-string/non-bytes type should raise a TypeError

def test_abort_with_custom_utf8_message():
    custom_message = "Custom message in UTF-8".encode("utf-8")
    with pytest.raises(SanicException):
        abort(400, custom_message)  # Providing a custom UTF-8 encoded message should work

def test_abort_with_default_utf8_message():
    with pytest.raises(SanicException):
        abort(500)  # Assuming 500 has a default message defined in STATUS_CODES, which is bytes and needs to be decoded
