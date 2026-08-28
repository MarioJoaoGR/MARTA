
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import import_module
import sys
import pytest

def test_import_math_module():
    math_module = import_module('math')
    assert hasattr(math_module, 'sqrt'), "The imported module should have a sqrt function."
    result = math_module.sqrt(16)
    assert result == 4.0, f"Expected the square root of 16 to be 4.0, but got {result}."

def test_import_custom_module():
    # Assuming there is a module named 'custom_module' in sys.modules for testing purposes
    with pytest.raises(ModuleNotFoundError):
        custom_module = import_module('custom_module')

def test_import_invalid_module():
    with pytest.raises(ImportError):
        import_module('invalid_module')
