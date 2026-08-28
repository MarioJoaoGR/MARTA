
from typing import Optional, Iterable, List
import pytest
from sanic.mixins.routes import RouteMixin


def test_missing_lines_to_cover():
    class MyRouteClass(RouteMixin):
        def __init__(self, name: str, strict_slashes: Optional[bool] = False):
            super().__init__(name=name, strict_slashes=strict_slashes)
    
    with pytest.raises(TypeError):
        my_instance = MyRouteClass()