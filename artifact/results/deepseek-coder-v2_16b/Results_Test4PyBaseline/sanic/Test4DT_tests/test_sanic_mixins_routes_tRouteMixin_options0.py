# Module: sanic.mixins.routes
# test_sanic_mixins_routes.py
from sanic.models.futures import FutureRoute
import pytest

@pytest.fixture
def route_mixin():
    class RouteMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_routes: set = set()
            self._future_statics: set = set()
            self.name = ""
            self.strict_slashes: bool = False

        def options(
            self,
            uri: str,
            host: Optional[str] = None,
            strict_slashes: Optional[bool] = None,
            version: Optional[int] = None,
            name: Optional[str] = None,
            ignore_body: bool = True,
        ):
            return self.route(
                uri,
                methods=frozenset({"OPTIONS"}),
                host=host,
                strict_slashes=strict_slashes,
                version=version,
                name=name,
                ignore_body=ignore_body,
            )

    return RouteMixin()

def test_route_mixin_initialization(route_mixin):
    assert hasattr(route_mixin, '_future_routes') and isinstance(route_mixin._future_routes, set)
    assert hasattr(route_mixin, '_future_statics') and isinstance(route_mixin._future_statics, set)
    assert hasattr(route_mixin, 'name') and route_mixin.name == ""
    assert hasattr(route_mixin, 'strict_slashes') and not route_mixin.strict_slashes

def test_options_method(route_mixin):
    result = route_mixin.options("/example", host="localhost", strict_slashes=True, name="example_route")
    assert isinstance(result, FutureRoute)
    assert result.uri == "/example"
    assert result.host == "localhost"
    assert result.strict_slashes is True
    assert result.name == "example_route"
    assert result.methods == frozenset({"OPTIONS"})

def test_options_method_with_default_values(route_mixin):
    result = route_mixin.options("/default")
    assert isinstance(result, FutureRoute)
    assert result.uri == "/default"
    assert result.host is None
    assert result.strict_slashes is False
    assert result.name is None
    assert result.methods == frozenset({"OPTIONS"})

def test_options_method_with_optional_parameters(route_mixin):
    result = route_mixin.options("/optional", host="example.com", strict_slashes=False, version=1)
    assert isinstance(result, FutureRoute)
    assert result.uri == "/optional"
    assert result.host == "example.com"
    assert not result.strict_slashes
    assert result.version == 1
    assert result.methods == frozenset({"OPTIONS"})
