
import pytest
from sanic import Sanic
from sanic.response import text

def has_message_body(status):
    return status not in (204, 304) and not (100 <= status < 200)

@pytest.fixture
def app():
    app = Sanic("TestApp")
    @app.route("/test")
    async def test_endpoint(request):
        return text("Response Body"), int(has_message_body(200))
    return app

def test_has_message_body_true():
    assert has_message_body(200) == True

def test_has_message_body_false_for_204():
    assert has_message_body(204) == False

def test_has_message_body_false_for_1xx():
    assert has_message_body(105) == False

def test_has_message_body_true_for_other_statuses():
    assert has_message_body(201) == True
    assert has_message_body(304) == False
    assert has_message_body(199) == False
