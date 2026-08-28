
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

# Test case for default initialization of ImportProcessor
def test_default_initialization():
    processor = ImportProcessor()
    assert isinstance(processor._lazy_import_class, type)
    assert processor._lazy_import_class == ImportReplacer

# Test case for custom lazy import class initialization
def test_custom_initialization():
    class CustomImportReplacer:
        def replace_import(self, module_name):
            pass
    
    processor = ImportProcessor(CustomImportReplacer)
    assert isinstance(processor._lazy_import_class, type)
    assert processor._lazy_import_class == CustomImportReplacer

# Test case for processing a valid import string
def test_valid_import_string():
    text_with_imports = """
    from math import sqrt
    import os as operating_system
    """
    processor = ImportProcessor()
    processor.imports = {}  # Initialize the imports dictionary if not already done
    processor._build_map(text_with_imports)