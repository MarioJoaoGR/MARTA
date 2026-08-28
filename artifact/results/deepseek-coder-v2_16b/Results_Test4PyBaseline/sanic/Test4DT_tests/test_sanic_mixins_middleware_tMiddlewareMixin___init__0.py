# Module: sanic.mixins.middleware
import pytest
from sanic import Sanic
from sanic.middleware import MiddlewareMixin
from typing import List

# Define a simple middleware function for testing
async def my_middleware(request):
    print("Request middleware executed!")

def test_middleware_mixin():
    # Create an instance of the mixin
    mixin = MiddlewareMixin()
    
    # Check that _future_middleware is initialized as an empty list
    assert hasattr(mixin, '_future_middleware')
    assert isinstance(mixin._future_middleware, List)
    assert len(mixin._future_middleware) == 0

def test_sanic_app_with_middleware():
    # Create a Sanic app instance
    app = Sanic("MyApp")
    
    # Register the middleware to be applied before each request
    app.register_middleware(my_middleware, 'request')
    
    # Define a route that will trigger the middleware
    @app.route('/')
    async def test(request):
        return "Hello, world!"
    
    # Run the Sanic app (this is just for demonstration purposes)
    # In a real test scenario, you might want to use a separate server or event loop
    # with pytest-asyncio or similar.
    # from sanic.testing import TestClient
    # client = TestClient(app)
    # response = await client.get('/')
    # assert response.status == 200
    # assert "Hello, world!" in (await response.text())

if __name__ == '__main__':
    pytest.main()
