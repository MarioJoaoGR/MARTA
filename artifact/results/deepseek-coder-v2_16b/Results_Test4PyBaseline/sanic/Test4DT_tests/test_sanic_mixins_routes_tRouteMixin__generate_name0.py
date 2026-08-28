# Module: sanic.mixins.routes
# test_sanic_mixins.py
from typing import Set
import pytest
from sanic import Sanic
from sanic.models.futures import FutureRoute, FutureStatic
from sanic.mixins import RouteMixin

@pytest.fixture(scope="module")
def app():
    return Sanic("MyApp")

@pytest.fixture()
def route_mixin():
    return RouteMixin()

def test_route_mixin_init(route_mixin):
    assert isinstance(route_mixin._future_routes, set)
    assert isinstance(route_mixin._future_statics, set)
    assert route_mixin.name == ""
    assert route_mixin.strict_slashes is False

def test_generate_name_with_string():
    mixin = RouteMixin()
    name = mixin._generate_name("specificName")
    assert name == "specificName"

def test_generate_name_with_object():
    class TestObject:
        name = "test_object_name"
    
    mixin = RouteMixin()
    name = mixin._generate_name(TestObject())
    assert name == "test_object_name"

def test_generate_name_with_none():
    mixin = RouteMixin()
    with pytest.raises(ValueError):
        mixin._generate_name()

def test_generate_name_with_invalid_object():
    class InvalidObject:
        pass
    
    mixin = RouteMixin()
    with pytest.raises(ValueError):
        mixin._generate_name(InvalidObject())

def test_generate_name_prefixed(route_mixin, app):
    route_mixin.name = "my_handler"
    name = route_mixin._generate_name("specificName")
    assert name == "my_handler.specificName"

def test_generate_name_already_prefixed(route_mixin, app):
    route_mixin.name = "existing_prefix"
    name = route_mixin._generate_name("existing_prefix.specificName")
    assert name == "existing_prefix.specificName"
