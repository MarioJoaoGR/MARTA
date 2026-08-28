# Module: sanic.mixins.middleware
import pytest
from sanic import Sanic
from sanic.middleware import MiddlewareType

# Define a simple middleware function
def my_middleware(get_response, scope):
    async def middleware(request):
        # Before request hook
        print("Before request hook")
        response = await get_response(request)
        # After request hook
        print("After request hook")
        return response
    return middleware

# Define a simple middleware function for the response stage
def my_middleware_response(get_response, scope):
    async def middleware(request):
        response = await get_response(request)
        # Before response hook
        print("Before response hook")
        return response
    return middleware

# Define a simple middleware function for a custom stage
def my_custom_stage_middleware(get_response, scope):
    async def middleware(request):
        # Before custom stage hook
        print("Before custom stage hook")
        response = await get_response(request)
        # After custom stage hook
        print("After custom stage hook")
        return response
    return middleware

# Test case for registering middleware to be applied at the request stage
def test_register_middleware_request():
    app = Sanic("MyApp")
    app.register_middleware(my_middleware, attach_to="request")
    
    @app.route("/")
    async def test(request):
        return "Hello, world!"
    
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == my_middleware
    assert app._future_middleware[0].attach_to == "request"

# Test case for registering middleware to be applied at the response stage
def test_register_middleware_response():
    app = Sanic("MyApp")
    app.register_middleware(my_middleware_response, attach_to="response")
    
    @app.route("/")
    async def test(request):
        return "Hello, world!"
    
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == my_middleware_response
    assert app._future_middleware[0].attach_to == "response"

# Test case for registering middleware to a custom stage
def test_register_middleware_custom():
    app = Sanic("MyApp")
    app.register_middleware(my_custom_stage_middleware, attach_to="custom_stage")
    
    @app.route("/")
    async def test(request):
        return "Hello, world!"
    
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == my_custom_stage_middleware
    assert app._future_middleware[0].attach_to == "custom_stage"
