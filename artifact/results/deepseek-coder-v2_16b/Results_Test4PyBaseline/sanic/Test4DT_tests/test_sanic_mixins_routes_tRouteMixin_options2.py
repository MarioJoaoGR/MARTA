
import pytest
from typing import Optional
from sanic import Sanic
from sanic.models.futures import FutureRoute

@pytest.fixture
def route_mixin():
    class RouteMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_routes: set = set()
            self._future_statics: set = set()
            self.name: str = ""
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