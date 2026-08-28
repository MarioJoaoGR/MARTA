# Module: sanic.mixins.routes
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.routerclass import Router
from typing import Optional, Set

# Import the RouteMixin class from the correct module
from sanic.mixins.routes import RouteMixin

def test_route_mixin_initialization():
    # Test initialization of RouteMixin without any arguments
    mixin = RouteMixin()
    assert isinstance(mixin._future_routes, set)
    assert isinstance(mixin._future_statics, set)
    assert mixin.name == ""
    assert mixin.strict_slashes is None

def test_route_mixin_with_arguments():
    # Test initialization of RouteMixin with arguments
    mixin = RouteMixin(name="test_route", strict_slashes=True)
    assert isinstance(mixin._future_routes, set)
    assert isinstance(mixin._future_statics, set)
    assert mixin.name == "test_route"
    assert mixin.strict_slashes is True

def test_get_method():
    app = Sanic("MyApp")
    router = Router()

    @app.route("/hello", methods=["GET"])
    async def hello_world(request):
        return text("Hello, World!")

    # Adding a route programmatically
    def custom_handler(request):
        return text("Custom route handler")
    router.add_route("/custom", ["GET"], custom_handler)

    with app.test_client() as client:
        response = client.get("/hello")
        assert response.status == 200
        assert response.text == "Hello, World!"

        # Test the custom route
        response = client.get("/custom")
        assert response.status == 200
        assert response.text == "Custom route handler"

def test_get_method_with_specifics():
    app = Sanic("MyApp")
    router = Router()

    @app.route("/hello", host="example.com", methods=["GET"], strict_slashes=True)
    async def hello_world(request):
        return text("Hello, World!")

    # Adding a route programmatically with specific host and strict slashes
    def custom_handler(request):
        return text("Custom route handler for specific host")
    router.add_route("/custom", ["GET"], custom_handler, host="example.com", strict_slashes=True)

    with app.test_client() as client:
        response = client.get("/hello", headers={"Host": "example.com"})
        assert response.status == 200
        assert response.text == "Hello, World!"

        # Test the custom route with specific host and strict slashes
        response = client.get("/custom", headers={"Host": "example.com"})
        assert response.status == 200
        assert response.text == "Custom route handler for specific host"

def test_get_method_with_versioning():
    app = Sanic("MyApp")
    router = Router()

    @app.route("/api/v1/hello", version=1, methods=["GET"], ignore_body=True)
    async def hello_world(request):
        return text("Hello, World!")

    # Adding a route programmatically with version and ignoring body
    def custom_handler(request):
        return text("Custom route handler for API v1")
    router.add_route("/api/v1/custom", ["GET"], custom_handler, version=1, ignore_body=True)

    with app.test_client() as client:
        response = client.get("/api/v1/hello")
        assert response.status == 200
        assert response.text == "Hello, World!"

        # Test the custom route with versioning and ignoring body
        response = client.get("/api/v1/custom")
        assert response.status == 200
        assert response.text == "Custom route handler for API v1"
