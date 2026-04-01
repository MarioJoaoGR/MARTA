
# pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_1_test_valid_case.py
from unittest import mock
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_valid_case():
    with mock.patch('pytutils.lazy.lazy_import.ImportReplacer', autospec=True) as MockImportReplacer:
        processor = ImportProcessor()
        assert isinstance(processor._lazy_import_class, ImportReplacer)
        
        # Test initialization with a custom lazy import class
        class CustomLazyImportClass:
            pass
        
        processor = ImportProcessor(lazy_import_class=CustomLazyImportClass)
        assert processor._lazy_import_class == CustomLazyImportClass
