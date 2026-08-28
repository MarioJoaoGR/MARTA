# Module: sanic.router
import pytest
from sanic.router import Router

# Fixture to create an instance of the Router class for testing
@pytest.fixture
def router():
    return Router()

# Test case to check if a default method is set correctly
def test_default_method(router):
    assert router.DEFAULT_METHOD == 'GET'

# Test case to check if allowed methods are set correctly
def test_allowed_methods(router):
    assert isinstance(router.ALLOWED_METHODS, list)
    assert len(router.ALLOWED_METHODS) > 0

# Test case to add a custom route and retrieve it
@pytest.mark.parametrize("path, methods, handler", [
    ("/custom", ["GET"], lambda request: request.json({"message": "Custom route"})),
])
def test_add_route(router, path, methods, handler):
    router.add(path, methods, handler)
    route_info = router.get(path=path, method="GET", host=None)
    assert route_info is not None
    assert callable(route_info['handler'])

# Test case to check if routes regex can be retrieved correctly
def test_routes_regex(router):
    regex_routes = router.routes_regex()
    assert isinstance(regex_routes, list)
    assert len(regex_routes) == 0  # Initially, there should be no routes

# Test case to check if adding a route updates the routes regex correctly
@pytest.mark.parametrize("path, methods, handler", [
    ("/hello", ["GET"], lambda request: request.json({"message": "Hello, World!"})),
])
def test_add_route_updates_regex(router, path, methods, handler):
    router.add(path, methods, handler)
    regex_routes = router.routes_regex()
    assert len(regex_routes) == 1
    assert regex_routes[0]['path'] == path
    assert regex_routes[0]['methods'] == methods

# Test case to check if retrieving a non-existent route raises NotFound exception
def test_get_non_existent_route(router):
    with pytest.raises(NotFound):
        router.get(path="/nonexistent", method="GET", host=None)
