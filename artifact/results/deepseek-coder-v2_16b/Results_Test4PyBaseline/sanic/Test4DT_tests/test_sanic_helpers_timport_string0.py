# Module: sanic.helpers
import pytest
from importlib import import_module
from types import ModuleType

# Import the function from the specified module
from sanic.helpers import import_string

def test_import_module():
    mod = import_string('os')
    assert isinstance(mod, ModuleType), "Expected a module object"

def test_import_class():
    cls = import_string('math.sqrt')
    assert callable(cls), "Expected a class instance or callable"

def test_import_from_specific_package():
    pkg_mod = import_string('os', 'posix')
    assert isinstance(pkg_mod, ModuleType), "Expected a module object from the specific package"

def test_invalid_module_name():
    with pytest.raises(ImportError):
        invalid_mod = import_string('invalid_module_name')
