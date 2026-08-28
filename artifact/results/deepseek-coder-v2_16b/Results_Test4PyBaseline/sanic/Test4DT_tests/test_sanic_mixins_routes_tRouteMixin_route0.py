# Module: sanic.mixins.routes
import pytest
from typing import List, Optional, Iterable
from sanic.mixins.routes import RouteMixin

# Assuming the module name is 'sanic.mixins.routes' and the class is defined in this file
from sanic.mixins.routes import RouteMixin as SanicRouteMixin

@pytest.fixture
def route_mixin():
    return SanicRouteMixin()

def test_route_mixin_init(route_mixin):
    assert isinstance(route_mixin._future_routes, set)
    assert isinstance(route_mixin._future_statics, set)
    assert route_mixin.name == ""
    assert route_mixin.strict_slashes is None

def test_route_method_with_default_parameters(route_mixin):
    @route_mixin.route('/test')
    def test_handler(request):
        return "Test"
    
    assert len(route_mixin._future_routes) == 1
    route = list(route_mixin._future_routes)[0]
    assert route.uri == '/test'
    assert route.methods == frozenset({'GET'})
    assert route.handler == test_handler

def test_route_method_with_specified_methods(route_mixin):
    @route_mixin.route('/test', methods=["POST"])
    def test_handler(request):
        return "Test"
    
    assert len(route_mixin._future_routes) == 1
    route = list(route_mixin._future_routes)[0]
    assert route.uri == '/test'
    assert route.methods == frozenset({'POST'})
    assert route.handler == test_handler

def test_route_method_with_strict_slashes(route_mixin):
    @route_mixin.route('/test', strict_slashes=True)
    def test_handler(request):
        return "Test"
    
    assert len(route_mixin._future_routes) == 1
    route = list(route_mixin._future_routes)[0]
    assert route.strict_slashes is True
    assert route.handler == test_handler

def test_route_method_with_websocket(route_mixin):
    @route_mixin.route('/test', websocket=True)
    def test_handler(ws, request):
        return "Test"
    
    assert len(route_mixin._future_routes) == 1
    route = list(route_mixin._future_routes)[0]
    assert route.websocket is True
    assert route.handler == test_handler

def test_route_method_with_static(route_mixin):
    @route_mixin.route('/test', static=True)
    def test_handler(request):
        return "Test"
    
    assert len(route_mixin._future_routes) == 1
    route = list(route_mixin._future_routes)[0]
    assert route.static is True
    assert route.handler == test_handler

def test_route_method_with_invalid_parameters():
    with pytest.raises(ValueError):
        class InvalidRouteMixin(SanicRouteMixin):
            @route('/test')  # Missing required parameter 'methods'
            def invalid_handler(self, request):
                return "Invalid"

def test_route_method_with_missing_request_parameter():
    with pytest.raises(ValueError):
        class InvalidRouteMixin(SanicRouteMixin):
            @route('/test', websocket=True)  # Missing required parameter 'ws' or 'request'
            def invalid_handler():
                return "Invalid"
