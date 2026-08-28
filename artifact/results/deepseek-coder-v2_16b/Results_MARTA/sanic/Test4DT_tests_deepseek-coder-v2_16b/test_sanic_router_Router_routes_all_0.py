
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.router import Router, HTTP_METHODS


def test_add_route():
    app = Sanic("MyApp")
    router = app.router
    
    @app.route("/example")
    async def example_handler(request):
        return text("Hello, world!")
    
    assert len(router.routes) == 1


