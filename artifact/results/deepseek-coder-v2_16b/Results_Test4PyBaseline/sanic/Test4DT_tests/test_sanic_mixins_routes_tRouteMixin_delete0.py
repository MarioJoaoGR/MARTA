# Module: sanic.mixins.routes
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.routerclass import Router
from sanic.models.futures import FutureRoute

# Import the RouteMixin class from the correct module
from sanic.mixins.routes import RouteMixin

@pytest.fixture(scope="module")
def app():
    app = Sanic("MyApp")
    router = Router()
    return app, router

def test_route_mixin_init(app):
    app, _ = app
    class MyRouteMixin(RouteMixin):
        def __init__(self, name: str, strict_slashes: bool = False, *args, **kwargs) -> None:
            super().__init__(*args, name=name, strict_slashes=strict_slashes, **kwargs)
    
    my_instance = MyRouteMixin("example_route", strict_slashes=True)
    assert my_instance.name == "example_route"
    assert my_instance.strict_slashes is True

def test_delete_method(app):
    app, router = app
    class MyRouteMixin(RouteMixin):
        def __init__(self, name: str, strict_slashes: bool = False, *args, **kwargs) -> None:
            super().__init__(*args, name=name, strict_slashes=strict_slashes, **kwargs)
        
        def delete(
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
                methods=frozenset({"DELETE"}),
                host=host,
                strict_slashes=strict_slashes,
                version=version,
                name=name,
                ignore_body=ignore_body,
            )
    
    my_instance = MyRouteMixin("example_route", strict_slashes=True)
    future_route = my_instance.delete(uri="/example", host="example.com", strict_slashes=True, version=1, name="example_route")
    
    assert isinstance(future_route, FutureRoute)
    assert future_route.uri == "/example"
    assert future_route.host == "example.com"
    assert future_route.strict_slashes is True
    assert future_route.version == 1
    assert future_route.name == "example_route"

def test_register_route(app):
    app, router = app
    class MyRouteMixin(RouteMixin):
        def __init__(self, name: str, strict_slashes: bool = False, *args, **kwargs) -> None:
            super().__init__(*args, name=name, strict_slashes=strict_slashes, **kwargs)
        
        @app.route("/example", methods=["DELETE"], host="example.com", strict_slashes=True, version=1, name="example_route")
        async def handle_request(self, request):
            return text("Example response")
    
    my_instance = MyRouteMixin("example_route", strict_slashes=True)
    app.blueprint(router)
    assert len(app._router.routes) == 1
    route = app._router.routes[0]
    assert route.uri == "/example"
    assert route.methods == frozenset({"DELETE"})
    assert route.host == "example.com"
    assert route.strict_slashes is True
    assert route.version == 1
    assert route.name == "example_route"
