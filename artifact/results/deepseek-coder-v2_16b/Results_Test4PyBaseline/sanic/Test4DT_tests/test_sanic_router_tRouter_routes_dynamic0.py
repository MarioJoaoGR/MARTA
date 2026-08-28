
# Module: sanic.router
import pytest
from sanic import Sanic
from sanic.router import Router
from sanic.exceptions import NotFound
from sanic.response import text

# Fixture to create an instance of the Sanic app and register the router
@pytest.fixture
def app():
    app = Sanic("MyApp")
    router = Router()
    app.blueprint(router)
    return app

# Test case for adding a route programmatically
def test_add_route_programmatically(app):
    def custom_handler(request):
        return text("Custom route response")
    
    app.router.add_route("/custom", ['GET'], custom_handler)
    
    # Check if the route is added correctly
    route_info = app.router.get(path="/custom", method="GET", host=None)
    assert route_info is not None, "Route should be found"
    assert route_info['handler'] == custom_handler, "Handler should match the added handler"

# Test case for retrieving a non-existent route
def test_get_non_existent_route(app):
    with pytest.raises(NotFound) as e:
        app.router.get(path="/nonexistent", method="GET", host=None)
    assert str(e.value) == "Requested URL /nonexistent not found"

# Test case for adding a route using a decorator and checking its presence
@pytest.mark.asyncio
async def test_add_route_using_decorator(app):
    @app.route("/hello", methods=['GET'])
    async def hello_handler(request):
        return text("Hello, World!")
    
    # Check if the route is added correctly
    route_info = app.router.get(path="/hello", method="GET", host=None)
    assert route_info is not None, "Route should be found"
    assert route_info['handler'].__name__ == 'hello_handler', "Handler should match the added handler"

# Test case for checking dynamic routes
def test_routes_dynamic(app):
    # Since this method returns a list of dynamic routes, we can check if it returns something non-empty
    dynamic_routes = app.router.routes_dynamic()
    assert len(dynamic_routes) > 0, "There should be at least one dynamic route"
