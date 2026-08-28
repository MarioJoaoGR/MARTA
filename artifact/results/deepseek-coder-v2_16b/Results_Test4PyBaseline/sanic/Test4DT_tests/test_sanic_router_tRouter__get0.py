
# Module: sanic.router
import pytest
from sanic.router import Router
from typing import Optional, Tuple, Dict, Any
from sanic.exceptions import NotFound, MethodNotSupported  # Importing exceptions explicitly

# Fixture to create a new instance of the Router class for each test
@pytest.fixture
def router():
    return Router()

# Test case for basic usage of the _get method
def test_basic_usage(router):
    route_info = router._get(path="/hello", method="GET", host=None)
    assert isinstance(route_info, tuple), "Expected a tuple"
    # Add more assertions to validate the structure and content of the returned tuple

# Test case for handling NotFound exception
def test_not_found_exception(router):
    with pytest.raises(NotFound) as exc_info:
        router._get(path="/notfound", method="POST", host=None)
    assert str(exc_info.value) == "Requested URL /notfound not found"

# Test case for handling MethodNotSupported exception
def test_method_not_supported_exception(router):
    with pytest.raises(MethodNotSupported) as exc_info:
        router._get(path="/hello", method="PUT", host=None)
    assert str(exc_info.value) == "Method PUT not allowed for URL /hello"

# Test case to check the behavior when no specific method is required
def test_no_specific_method(router):
    route_info = router._get(path="/hello", method="GET", host=None)
    assert isinstance(route_info, tuple), "Expected a tuple"
    # Add more assertions to validate the structure and content of the returned tuple

# Test case to check the behavior when specifying a host
def test_specify_host(router):
    route_info = router._get(path="/hello", method="GET", host="example.com")
    assert isinstance(route_info, tuple), "Expected a tuple"
    # Add more assertions to validate the structure and content of the returned tuple
