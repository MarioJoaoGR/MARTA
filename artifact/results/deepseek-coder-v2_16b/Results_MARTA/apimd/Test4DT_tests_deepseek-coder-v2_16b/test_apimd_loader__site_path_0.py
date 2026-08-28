
import pytest
from importlib.util import find_spec
from os.path import dirname

def _site_path(name: str) -> str:
    """Get the path in site-packages if exist."""
    s = find_spec(name)
    if s is None or s.submodule_search_locations is None:
        return ""
    return dirname(s.submodule_search_locations[0])

# Test scenarios

def test_valid_input():
    # Setup: Real instance of find_spec with valid arguments
    spec = find_spec('numpy')
    assert _site_path('numpy') == dirname(spec.submodule_search_locations[0])

def test_missing_module():
    # Setup: Real instance of find_spec with non-existent module name
    spec = find_spec('nonexistentmodule')
    assert _site_path('nonexistentmodule') == ""

def test_invalid_input():
    # Setup: None
    with pytest.raises(TypeError):
        _site_path()
