
import pytest
from sanic.mixins.routes import RouteMixin
from typing import Set, Optional, Iterable, List

class FutureRoute:
    handler: str
    uri: str
    methods: Optional[Iterable[str]]
    host: str
    strict_slashes: bool
    stream: bool
    version: Optional[int]
    name: str
    ignore_body: bool
    websocket: bool
    subprotocols: Optional[List[str]]
    unquote: bool
    static: bool

class FutureStatic:
    pass

class MyClass(RouteMixin):
    def __init__(self, name: str, strict_slashes: Optional[bool] = False):
        super().__init__(name=name, strict_slashes=strict_slashes)


def test_default_values():
    instance = MyClass("default_route")
    assert instance.strict_slashes is False