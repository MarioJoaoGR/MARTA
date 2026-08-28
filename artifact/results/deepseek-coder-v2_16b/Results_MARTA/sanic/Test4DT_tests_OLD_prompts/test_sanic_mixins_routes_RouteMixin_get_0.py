
import pytest
from unittest.mock import patch, MagicMock
from sanic.mixins.routes import RouteMixin
from typing import Optional, Set

class FutureRoute:
    pass

class FutureStatic:
    pass

@pytest.fixture(name="route_mixin")
def create_route_mixin():
    return RouteMixin()

@pytest.mark.parametrize("uri, host, strict_slashes, version, name", [
    ("/example", "localhost", True, None, "example_route"),
    ("/test", None, False, 1, "test_route")
])
def test_get_method(route_mixin, uri, host, strict_slashes, version, name):
    with patch.object(RouteMixin, 'route', return_value=MagicMock()) as mock_route:
        route_mixin.get(uri, host, strict_slashes, version, name)
        mock_route.assert_called_once_with(
            uri,
            methods=frozenset({"GET"}),
            host=host,
            strict_slashes=strict_slashes,
            version=version,
            name=name,
            ignore_body=True
        )
