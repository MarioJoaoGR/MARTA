
import pytest
from sanic import Sanic
from sanic.router import Router
from sanic.exceptions import NotFound  # Importing NotFound from sanic.exceptions

# Fixture to create an instance of Router for testing
@pytest.fixture
def router():
    return Router()

def test_default_method(router):
    assert router.DEFAULT_METHOD == 'GET'

def test_allowed_methods(router):
    assert isinstance(router.ALLOWED_METHODS, list)
    assert len(router.ALLOWED_METHODS) > 0

def test_routes_static_returns_list(router):
    routes = router.routes_static()
    assert isinstance(routes, list)

def test_routes_static_empty_by_default(router):
    assert len(router.routes_static()) == 0

def test_add_route_and_get_route(router):
    def custom_handler(request):
        return request.json({"message": "Custom route"})
    
    with pytest.raises(NotFound):
        router.get(path="/custom", method="GET", host=None)
    
    router.add_route("/custom", ['GET'], custom_handler)
    try:
        route_info = router.get(path="/custom", method="GET", host=None)
        assert route_info is not None
    except NotFound as e:
        pytest.fail("Expected route to be found but got an exception: {}".format(e))
