# Module: sanic.mixins.routes
# test_sanic_mixins_routes.py
from sanic.mixins.routes import RouteMixin
import pytest
from typing import Set, Union, PurePath
from unittest.mock import patch

@pytest.fixture
def route_mixin():
    return RouteMixin()

class TestRouteMixin:
    
    def test_init(self, route_mixin):
        assert isinstance(route_mixin._future_routes, set)
        assert isinstance(route_mixin._future_statics, set)
        assert route_mixin.name == ""
        assert route_mixin.strict_slashes is None
    
    @pytest.mark.parametrize("file_or_directory", [
        "path/to/file", 
        b"bytes", 
        PurePath("pure_path")
    ])
    def test_static_valid_paths(self, route_mixin, file_or_directory):
        with pytest.raises(ValueError):
            route_mixin.static("uri", file_or_directory)
    
    @pytest.mark.parametrize("strict_slashes", [True, False])
    def test_static_with_strict_slashes(self, route_mixin, strict_slashes):
        with patch.object(route_mixin, 'strict_slashes', new=strict_slashes):
            route_mixin.static("uri", "path/to/file")
            assert len(route_mixin._future_statics) == 1
    
    def test_static_invalid_type(self, route_mixin):
        with pytest.raises(ValueError):
            route_mixin.static("uri", object())
    
    @pytest.mark.parametrize("apply", [True, False])
    def test_static_apply(self, route_mixin, apply):
        route_mixin.static("uri", "path/to/file", apply=apply)
        if apply:
            assert len(route_mixin._future_statics) == 1
        else:
            assert len(route_mixin._future_statics) == 0
    
    def test_static_generate_name(self, route_mixin):
        result = route_mixin._generate_name("test_name")
        assert result == "test_name"
