# Module: sanic.mixins.middleware
import pytest
from typing import List
from functools import partial
from sanic import Sanic
from sanic.middleware import MiddlewareMixin

class FutureMiddleware:
    def __init__(self, middleware: callable, attach_to: str):
        self.middleware = middleware
        self.attach_to = attach_to

class MyMiddlewareClass(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _apply_middleware(self, middleware: FutureMiddleware):
        print("Applying middleware!")

# Fixture to create a Sanic app instance for testing
@pytest.fixture
def sanic_app():
    return Sanic("MyApp")

# Test case for MiddlewareMixin initialization
def test_middleware_mixin_initialization():
    my_middleware = MyMiddlewareClass()
    assert hasattr(my_middleware, '_future_middleware')
    assert isinstance(my_middleware._future_middleware, list)
    assert len(my_middleware._future_middleware) == 0

# Test case for on_request method with callable middleware
def test_on_request_with_callable_middleware(sanic_app):
    def my_middleware(request):
        pass

    my_middleware = MyMiddlewareClass()
    handle_request = my_middleware.on_request(my_middleware)
    assert callable(handle_request)

# Test case for on_request method without middleware
def test_on_request_without_middleware(sanic_app):
    my_middleware = MyMiddlewareClass()
    handle_request = my_middleware.on_request()
    assert isinstance(handle_request, partial)
    assert callable(handle_request.func)

# Test case for applying middleware to a Sanic app
def test_apply_middleware_to_sanic_app(sanic_app):
    def my_middleware(request):
        pass

    my_middleware = MyMiddlewareClass()
    sanic_app.blueprint(my_middleware)
    assert len(sanic_app._middlewares['request']) == 1
    assert sanic_app._middlewares['request'][0].middleware == my_middleware

# Test case for applying middleware to a specific attach point
def test_apply_middleware_to_specific_attach_point(sanic_app):
    def request_middleware(request):
        pass

    def response_middleware(response):
        pass

    my_middleware = MyMiddlewareClass()
    sanic_app.blueprint(my_middleware)
    assert len(sanic_app._middlewares['request']) == 1
    assert len(sanic_app._middlewares['response']) == 0

# Test case for applying middleware to a BlueprintGroup
def test_apply_middleware_to_blueprintgroup(sanic_app):
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    def request_middleware(request):
        pass

    my_middleware = MyMiddlewareClass()
    sanic_app.blueprint(bpg)
    assert len(sanic_app._middlewares['request']) == 2
    assert sanic_app._middlewares['request'][0].middleware == request_middleware
    assert sanic_app._middlewares['request'][1].middleware == request_middleware
