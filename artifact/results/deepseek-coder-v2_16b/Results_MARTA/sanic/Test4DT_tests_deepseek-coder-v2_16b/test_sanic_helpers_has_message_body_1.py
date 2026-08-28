
import pytest
from sanic import Sanic
from sanic.response import text

def has_message_body(status):
    return status not in (204, 304) and not (100 <= status < 200)

@pytest.fixture
def app():
    app = Sanic("TestApp")
    @app.route("/test")
    async def test_route(request):
        return text("Hello, world!", status=404)
    return app

def test_has_message_body_true_for_valid_status():
    assert has_message_body(200) is True

def test_has_message_body_false_for_204_status():
    assert has_message_body(204) is False

def test_has_message_body_false_for_1xx_range():
    assert has_message_body(105) is False
