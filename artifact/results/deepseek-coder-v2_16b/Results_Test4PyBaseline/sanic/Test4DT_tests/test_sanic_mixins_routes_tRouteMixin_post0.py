# Module: sanic.mixins.routes
# test_sanic_mixins_routes.py
from sanic.mixins.routes import RouteMixin
import pytest
from typing import Optional, Set

@pytest.fixture
def route_mixin():
    return RouteMixin()

def test_route_mixin_initialization(route_mixin):
    assert isinstance(route_mixin._future_routes, set)
    assert isinstance(route_mixin._future_statics, set)
    assert route_mixin.name == ""
    assert route_mixin.strict_slashes is None

def test_post_method_basic(route_mixin):
    @route_mixin.post("/test")
    def handler(request):
        return "Test"
    
    # Check if the post method adds a route correctly
    assert len(route_mixin._future_routes) == 1
    future_route = list(route_mixin._future_routes)[0]
    assert future_route.uri == "/test"
    assert future_route.methods == frozenset({"POST"})
    assert future_route.host is None
    assert future_route.strict_slashes is False
    assert not future_route.stream
    assert future_route.version is None
    assert future_route.name is None

def test_post_method_with_parameters(route_mixin):
    @route_mixin.post("/test", host="example.com", strict_slashes=True, stream=True, version=1, name="test_route")
    def handler(request):
        return "Test"
    
    # Check if the post method adds a route correctly with all parameters set
    assert len(route_mixin._future_routes) == 1
    future_route = list(route_mixin._future_routes)[0]
    assert future_route.uri == "/test"
    assert future_route.methods == frozenset({"POST"})
    assert future_route.host == "example.com"
    assert future_route.strict_slashes is True
    assert future_route.stream
    assert future_route.version == 1
    assert future_route.name == "test_route"

def test_post_method_without_parameters(route_mixin):
    @route_mixin.post("/test")
    def handler(request):
        return "Test"
    
    # Check if the post method adds a route correctly without parameters
    assert len(route_mixin._future_routes) == 1
    future_route = list(route_mixin._future_routes)[0]
    assert future_route.uri == "/test"
    assert future_route.methods == frozenset({"POST"})
    assert future_route.host is None
    assert future_route.strict_slashes is False
    assert not future_route.stream
    assert future_route.version is None
    assert future_route.name is None
