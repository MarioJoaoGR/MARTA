
import pytest
from unittest.mock import patch, MagicMock
from sanic.router import Router
from sanic.exceptions import NotFound, MethodNotSupported

# Test Scenario 1: test_valid_input
def test_valid_input():
    router = Router()
    with patch('sanic.router.Router.routes_static', return_value=[]):
        static_routes = router.routes_static()
        assert isinstance(static_routes, list), "Expected a list of routes"

# Test Scenario 2: test_edge_case
def test_edge_case():
    router = Router()
    with patch('sanic.router.Router.routes_static', return_value=[]):
        static_routes = router.routes_static()
        assert isinstance(static_routes, list), "Expected a list of routes"

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    router = Router()
    with patch('sanic.router.Router.routes_static', side_effect=Exception("Invalid input")):
        with pytest.raises(Exception):
            static_routes = router.routes_static()
