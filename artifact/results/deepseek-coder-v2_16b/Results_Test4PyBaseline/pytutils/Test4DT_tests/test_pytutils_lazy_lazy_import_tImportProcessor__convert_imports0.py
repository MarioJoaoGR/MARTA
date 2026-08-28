
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from pytutils.lazy.lazy_import import ImportProcessor

def test_default_import():
    processor = ImportProcessor()
    assert hasattr(processor, '_lazy_import_class')
    assert isinstance(processor._lazy_import_class, type)

def test_custom_import():
    class CustomImportReplacer:
        def replace_import(self, module_name):
            pass
    
    processor = ImportProcessor(CustomImportReplacer)
    assert hasattr(processor, '_lazy_import_class')
    assert isinstance(processor._lazy_import_class, type)
    assert issubclass(processor._lazy_import_class, CustomImportReplacer)

def test_build_map():
    processor = ImportProcessor()
    text_with_imports = """
    from math import sqrt
    import os as operating_system
    """
    processor.imports = {}  # Initialize the imports dictionary if not already done
    processor._build_map(text_with_imports)