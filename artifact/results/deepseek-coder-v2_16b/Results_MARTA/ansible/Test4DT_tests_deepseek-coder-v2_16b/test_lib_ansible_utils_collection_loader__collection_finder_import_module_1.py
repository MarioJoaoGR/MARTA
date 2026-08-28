
import pytest
import sys
from ansible.utils.collection_loader._collection_finder import import_module

def test_import_existing_module():
    module = import_module('math')
    assert module is not None, "Imported module should be a valid object"
    assert hasattr(module, 'sqrt'), f"Module {module} does not have the expected attribute 'sqrt'"
    assert callable(getattr(module, 'sqrt')), f"Attribute 'sqrt' of module {module} is not callable"
    result = module.sqrt(16)
    assert result == 4.0, f"Expected sqrt(16) to be 4.0, but got {result}"

def test_import_non_existing_module():
    with pytest.raises(ImportError):
        import_module('nonexistent_module')
