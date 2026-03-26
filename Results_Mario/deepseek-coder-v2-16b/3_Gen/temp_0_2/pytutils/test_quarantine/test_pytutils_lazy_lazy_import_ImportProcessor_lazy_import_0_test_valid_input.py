
from pytutils.lazy.lazy_import import ImportReplacer
from unittest.mock import patch
import pytest

@pytest.fixture
def processor():
    return ImportProcessor()

@patch('pytutils.lazy.lazy_import.ImportReplacer')
def test_default_lazy_import_class(mock_ImportReplacer, processor):
    with patch.object(ImportProcessor, '_build_map', autospec=True) as mock_build_map:
        with patch.object(ImportProcessor, '_convert_imports', autospec=True) as mock_convert_imports:
            scope = {}
            text = """
            from bzrlib import (
                foo,
                bar,
                baz,
            )
            import bzrlib.branch
            import bzrlib.transport
            """
            processor.lazy_import(scope, text)
            
            mock_build_map.assert_called_once()
            mock_convert_imports.assert_called_once_with(scope)
            assert isinstance(processor._lazy_import_class, ImportReplacer)

@patch('pytutils.lazy.lazy_import.CustomImportReplacer')
def test_custom_lazy_import_class(mock_CustomImportReplacer):
    processor = ImportProcessor(lazy_import_class=mock_CustomImportReplacer)
    assert isinstance(processor._lazy_import_class, mock_CustomImportReplacer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor_lazy_import_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor_lazy_import_0_test_valid_input.py:8:11: E0602: Undefined variable 'ImportProcessor' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor_lazy_import_0_test_valid_input.py:12:22: E0602: Undefined variable 'ImportProcessor' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor_lazy_import_0_test_valid_input.py:13:26: E0602: Undefined variable 'ImportProcessor' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor_lazy_import_0_test_valid_input.py:32:16: E0602: Undefined variable 'ImportProcessor' (undefined-variable)


"""