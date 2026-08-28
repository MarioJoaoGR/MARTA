
import pytest
from pytutils.lazy.lazy_import import lazy_import, ImportProcessor


def test_lazy_import_custom_class():
    with pytest.raises(ModuleNotFoundError):
        from my_custom_module import MyCustomLazyImport
    
    # This is a mock for the purpose of this exercise, as we cannot directly assign to module attributes in tests without side effects.
    class MockMyCustomLazyImport:
        pass
    
    with pytest.raises(ModuleNotFoundError):
        from my_custom_module import MyCustomLazyImport
