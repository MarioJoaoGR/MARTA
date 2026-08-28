
import pytest
from sanic import Sanic
from sanic.router import Router

def test_valid_routes():
    app = Sanic("TestApp")
    router = app.router
    with pytest.raises(AttributeError):
        router.configure_routes([
            (r"/route1", "handler1"),
            (r"/route2", "handler2")
        ])

