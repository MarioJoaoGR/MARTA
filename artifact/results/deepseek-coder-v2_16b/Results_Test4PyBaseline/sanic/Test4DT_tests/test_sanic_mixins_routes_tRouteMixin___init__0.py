
# Module: sanic.mixins.routes
# test_route_mixin.py
from sanic import Sanic
from sanic.response import text
from typing import Set, Optional
import pytest

@pytest.fixture(scope="module")
def app():
    return Sanic("MyApp")

class FutureRoute:
    def __init__(self, handler, uri, host=None, strict_slashes=False, stream=False, name=None, methods=None, version=None, ignore_body=False, websocket=False, subprotocols=None, unquote=False, static=False):
        self.handler = handler
        self.uri = uri
        self.host = host
        self.strict_slashes = strict_slashes
        self.stream = stream
        self.name = name
        self.methods = methods or ["GET"]
        self.version = version
        self.ignore_body = ignore_body
        self.websocket = websocket
        self.subprotocols = subprotocols or []
        self.unquote = unquote
        self.static = static

    def blueprint(self, app):
        if self.methods:
            for method in self.methods:
                app.route(self.uri, methods=[method])(self.handler)
        else:
            app.route(self.uri)(self.handler)

class FutureStatic:
    def __init__(self, uri, file_or_directory, pattern, use_modified_since, use_content_range, stream_large_files, name, host=None, strict_slashes=False, content_type=True):
        self.uri = uri
        self.file_or_directory = file_or_directory
        self.pattern = pattern
        self.use_modified_since = use_modified_since
        self.use_content_range = use_content_range
        self.stream_large_files = stream_large_files
        self.name = name
        self.host = host
        self.strict_slashes = strict_slashes
        self.content_type = content_type

    def serve(self, request):
        return text("Serving static file")

class RouteMixin:
    def __init__(self, *args, **kwargs) -> None:
        self._future_routes: Set[FutureRoute] = set()
        self._future_statics: Set[FutureStatic] = set()
        self.name: Optional[str] = None
        self.strict_slashes: Optional[bool] = False

    def blueprint(self, app):
        for route in self._future_routes:
            route.blueprint(app)

class MyClass(RouteMixin):
    def __init__(self, name: str, strict_slashes: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, name=name, strict_slashes=strict_slashes, **kwargs)

def test_basic_initialization():
    future_route = FutureRoute(
        handler="my_handler",
        uri="/my/uri",
        host="example.com",
        strict_slashes=True,
        stream=False,
        name="my_route"
    )
    assert future_route.handler == "my_handler"
    assert future_route.uri == "/my/uri"
    assert future_route.host == "example.com"
    assert future_route.strict_slashes is True
    assert future_route.stream is False
    assert future_route.name == "my_route"

def test_initialization_with_optional_parameters():
    future_route = FutureRoute(
        handler="my_handler",
        uri="/optional/uri",
        host="example.com",
        strict_slashes=True,
        stream=False,
        name="optional_route",
        methods=["GET"],
        version=1,
        ignore_body=True,
        websocket=True,
        subprotocols=["ws"],
        unquote=True,
        static=False
    )
    assert future_route.handler == "my_handler"
    assert future_route.uri == "/optional/uri"
    assert future_route.host == "example.com"
    assert future_route.strict_slashes is True
    assert future_route.stream is False
    assert future_route.name == "optional_route"
    assert future_route.methods == ["GET"]
    assert future_route.version == 1
    assert future_route.ignore_body is True
    assert future_route.websocket is True
    assert future_route.subprotocols == ["ws"]
    assert future_route.unquote is True
    assert future_route.static is False

def test_using_futureroute_in_subclassed_class():
    my_instance = MyClass("example_route", strict_slashes=True)