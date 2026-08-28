
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.router import Router as SanicRouter

@pytest.fixture(scope="module")
def app():
    app = Sanic("TestApp")
    router = app.router
    return app, router

def test_default_method(app):
    _, router = app
    assert router.DEFAULT_METHOD == 'GET'

