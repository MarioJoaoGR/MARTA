# Module: sanic.mixins.routes
# test_route_mixin.py
from sanic import Sanic
from sanic.response import text
from sanic.blueprints import Blueprint
from sanic.models.futures import FutureRoute
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("MyApp")
    bp = Blueprint('my_blueprint', url_prefix='/api')
    
    @bp.route('/hello', methods=["GET"])
    def hello_world(request):
        return text("Hello, World!")
    
    app.blueprint(bp)
    yield app

def test_add_route_with_default_methods(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    my_instance = MyRouteMixin("example_route", strict_slashes=True)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is True

def test_add_route_with_specified_methods(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET", "POST"])
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=True)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is True
    assert len(my_instance._future_routes) == 1
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET", "POST"}

def test_add_route_with_strict_slashes_default(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"])
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}

def test_add_route_with_strict_slashes_specified(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"], strict_slashes=True)
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}
    assert route.strict_slashes is True

def test_add_route_with_host(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"], host="localhost")
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}
    assert route.host == "localhost"

def test_add_route_with_version(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"], version=1)
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}
    assert route.version == 1

def test_add_route_with_name(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"], name="hello")
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}
    assert route.name == "hello"

def test_add_route_with_stream(app):
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
    
    @MyRouteMixin.route('/hello', methods=["GET"], stream=True)
    def hello_world(request):
        return text("Hello, World!")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=False)
    assert hasattr(my_instance, 'name')
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is False
    route = list(my_instance._future_routes)[0]
    assert set(route.methods) == {"GET"}
    assert route.stream is True
