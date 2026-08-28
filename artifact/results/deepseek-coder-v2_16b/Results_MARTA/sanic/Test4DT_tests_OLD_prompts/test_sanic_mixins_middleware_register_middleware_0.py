
import pytest
from sanic import Sanic
from sanic.response import text
from unittest.mock import patch, MagicMock

# Test scenario 1: Registering a request middleware function
@pytest.mark.asyncio
async def test_register_request_middleware():
    app = Sanic("TestApp")
    
    # Define the middleware function
    async def my_middleware(get_response, scope):
        assert scope["type"] == "http"
        response = await get_response(scope)
        return response
    
    with patch('sanic.mixins.middleware.FutureMiddleware', new=MagicMock()):
        app.register_middleware(my_middleware, attach_to="request")
        
        @app.route("/test")
        async def test_handler(request):
            return text("Hello, world!")
        
        request = MagicMock()
        request.headers = {}
        response = await app.request_class(app, "GET", "/test", headers=request.headers)
        assert response.text == "Hello, world!"

# Test scenario 2: Registering a response middleware function
@pytest.mark.asyncio
async def test_register_response_middleware():
    app = Sanic("TestApp")
    
    # Define the middleware function
    async def my_middleware(get_response, scope):
        response = await get_response(scope)
        assert "Hello" in response.text
        return response
    
    with patch('sanic.mixins.middleware.FutureMiddleware', new=MagicMock()):
        app.register_middleware(my_middleware, attach_to="response")
        
        @app.route("/test")
        async def test_handler(request):
            return text("Hello, world!")
        
        request = MagicMock()
        request.headers = {}
        response = await app.request_class(app, "GET", "/test", headers=request.headers)
        assert "Hello" in response.text

# Test scenario 3: Registering a middleware class
@pytest.mark.asyncio
async def test_register_middleware_class():
    app = Sanic("TestApp")
    
    # Define the middleware class
    class MyMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
        
        async def __call__(self, scope):
            response = await self.get_response(scope)
            assert "Hello" in response.text
            return response
    
    with patch('sanic.mixins.middleware.FutureMiddleware', new=MagicMock()):
        app.register_middleware(MyMiddleware, attach_to="request")
        
        @app.route("/test")
        async def test_handler(request):
            return text("Hello, world!")
        
        request = MagicMock()
        request.headers = {}
        response = await app.request_class(app, "GET", "/test", headers=request.headers)
        assert "Hello" in response.text
