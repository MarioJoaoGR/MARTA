
import pytest
from sanic import Sanic
from sanic.router import Router

def test_valid_input():
    app = Sanic("TestApp")
    router = app.router
    with pytest.raises(AttributeError):
        router.add_route('GET', '/test', lambda req: None)

def test_edge_case():
    router = Router()
    with pytest.raises(TypeError):
        matched_handler = router.routes_regex()

def test_invalid_input():
    with pytest.raises(AttributeError):
        router = Router()
        router.configure_routes('invalid_route', 'handler')
