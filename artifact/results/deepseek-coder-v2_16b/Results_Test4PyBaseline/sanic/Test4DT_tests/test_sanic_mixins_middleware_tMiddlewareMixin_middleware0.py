# Module: sanic.mixins.middleware
# test_sanic_middleware.py
from sanic import Sanic
from sanic.middleware import MiddlewareMixin
from functools import partial
import pytest

class FutureMiddleware:
    def __init__(self, middleware, attach_to="request"):
        self.middleware = middleware
        self.attach_to = attach_to

class MyMiddlewareClass(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _apply_middleware(self, middleware: FutureMiddleware):
        print("Applying custom middleware!")

# Test initialization of MiddlewareMixin subclass
def test_middleware_mixin_initialization():
    my_middleware = MyMiddlewareClass()
    assert hasattr(my_middleware, '_future_middleware')
    assert isinstance(my_middleware._future_middleware, list)

# Test decorating middleware function with @app.middleware('request')
@pytest.mark.asyncio
async def test_decorating_middleware():
    app = Sanic("MyApp")
    
    @app.middleware('request')
    async def my_custom_middleware(request):
        print("Request middleware executed!")
        return request  # Return the modified request if necessary

    class MyMiddlewareClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            print("Applying custom middleware!")

    my_middleware = MyMiddlewareClass()
    app.blueprint(my_middleware)
    
    # Add assertions to verify the behavior of the middleware registration and application
    assert len(my_middleware._future_middleware) == 1
    await app.test_client.get('/')
    captured_output = capsys.readouterr().out
    assert "Request middleware executed!" in captured_output

# Test creating an instance of MyMiddlewareClass and attaching it to a Sanic app
def test_attaching_to_sanic_app():
    app = Sanic("MyApp")
    my_middleware = MyMiddlewareClass()
    app.blueprint(my_middleware)
    
    # Add assertions to verify the behavior of the middleware registration and application
    assert len(my_middleware._future_middleware) == 0  # Initially empty, should be populated by _apply_middleware call
    my_middleware._future_middleware = [FutureMiddleware(lambda x: x)]  # Mocking the future middleware list for test purposes
    app.run()
    captured_output = capsys.readouterr().out
    assert "Applying custom middleware!" in captured_output
