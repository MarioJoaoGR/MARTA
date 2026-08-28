
import pytest
from sanic.mixins.routes import RouteMixin
from typing import Set, Optional

class FutureRoute:
    pass

class FutureStatic:
    pass

@pytest.fixture
def route_mixin():
    return RouteMixin()


def test_delete_method(route_mixin):
    result = route_mixin.delete("/example", host="example.com")
    assert result is not None