# Module: sanic.mixins.middleware
import pytest
from sanic import Sanic
from sanic.response import text
from functools import partial
from typing import List

# Import the MiddlewareMixin class from the specified module
from sanic.mixins.middleware import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

def test_middleware_mixin_initialization():
    my_middleware = MyMiddleware()
    assert hasattr(my_middleware, '_future_middleware')
    assert isinstance(my_middleware._future_middleware, list)
    assert len(my_middleware._future_middleware) == 0

def test_attach_middleware_to_request():
    app = Sanic("TestApp")
    
    @app.middleware('request')
    async def request_middleware(request):
        pass
    
    my_middleware = MyMiddleware()
    app.blueprint(my_middleware)
    
    assert len(app._middlewares['request']) == 1
    assert isinstance(app._middlewares['request'][0], partial)
    assert app._middlewares['request'][0].func == request_middleware

def test_attach_middleware_to_response():
    app = Sanic("TestApp")
    
    @app.middleware('response')
    async def response_middleware(request, response):
        pass
    
    my_middleware = MyMiddleware()
    app.blueprint(my_middleware)
    
    assert len(app._middlewares['response']) == 1
    assert isinstance(app._middlewares['response'][0], partial)
    assert app._middlewares['response'][0].func == response_middleware

def test_on_response_with_middleware():
    app = Sanic("TestApp")
    
    def middleware_function(request, response):
        pass
    
    my_middleware = MyMiddleware()
    result = my_middleware.on_response(middleware_function)
    
    assert callable(result)
    assert result.func == middleware_function

def test_on_response_without_middleware():
    app = Sanic("TestApp")
    
    my_middleware = MyMiddleware()
    result = my_middleware.on_response()
    
    assert callable(result)
    assert isinstance(result, partial)
    assert result.func == my_middleware.middleware
    assert result.args == ()
    assert result.keywords == {'attach_to': 'response'}

if __name__ == '__main__':
    pytest.main()
