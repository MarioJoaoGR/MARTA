
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

# Test cases for ImportProcessor class

def test_default_init():
    processor = ImportProcessor()
    assert hasattr(processor, 'imports')
    assert isinstance(processor._lazy_import_class, type)
    assert issubclass(processor._lazy_import_class, ImportReplacer)

def test_custom_init():
    class CustomImportReplacer(ImportReplacer):
        def replace_import(self, module_name):
            pass
    
    processor = ImportProcessor(CustomImportReplacer)
    assert hasattr(processor, 'imports')