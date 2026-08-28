# Module: sanic.mixins.routes
# test_sanic_mixins_routes.py
from sanic.mixins.routes import RouteMixin
import pytest
from typing import Optional, Set

@pytest.fixture(scope="module")
def route_mixin():
    return RouteMixin()

class TestRouteMixin:
    
    def test_init(self, route_mixin):
        assert isinstance(route_mixin._future_routes, set)
        assert isinstance(route_mixin._future_statics, set)
        assert route_mixin.name == ""
        assert route_mixin.strict_slashes is None
    
    @pytest.mark.parametrize("uri, host, strict_slashes, stream, version, name", [
        ("/api/v1/resource", None, None, False, None, None),
        ("/hello", "example.com", True, True, 1, "hello"),
    ])
    def test_put(self, route_mixin, uri, host, strict_slashes, stream, version, name):
        result = route_mixin.put(uri, host=host, strict_slashes=strict_slashes, stream=stream, version=version, name=name)
        assert isinstance(result, RouteMixin)
