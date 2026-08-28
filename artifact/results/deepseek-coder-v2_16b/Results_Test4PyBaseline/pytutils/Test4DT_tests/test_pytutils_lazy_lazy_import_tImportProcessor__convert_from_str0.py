
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from pytutils.lazy.lazy_import import ImportProcessor
import math  # Added missing import for 'math'
import os    # Added missing import for 'os'

def test_default_import_processor():
    processor = ImportProcessor()
    assert hasattr(processor, 'imports'), "ImportProcessor should have an 'imports' attribute"
    assert hasattr(processor, '_lazy_import_class'), "ImportProcessor should have a '_lazy_import_class' attribute"
    assert isinstance(processor._lazy_import_class, type), "Default _lazy_import_class should be a class"

def test_custom_import_processor():
    class CustomImportReplacer:
        def replace_import(self, module_name):
            pass
    
    processor = ImportProcessor(CustomImportReplacer)
    assert hasattr(processor, 'imports'), "ImportProcessor should have an 'imports' attribute"