
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from pytutils.lazy.lazy_import import ImportProcessor

def test_default_usage():
    processor = ImportProcessor()
    assert hasattr(processor, 'imports')
    assert hasattr(processor, '_lazy_import_class')
    assert isinstance(processor._lazy_import_class, type)

def test_custom_class_usage():
    class CustomImportReplacer:
        def replace_import(self, module_name):
            pass
    
    processor = ImportProcessor(CustomImportReplacer)
    assert hasattr(processor, 'imports')