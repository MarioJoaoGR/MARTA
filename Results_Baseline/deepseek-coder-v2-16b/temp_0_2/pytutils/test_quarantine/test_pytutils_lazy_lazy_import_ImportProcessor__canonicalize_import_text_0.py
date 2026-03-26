
# Module: pytutils.lazy.lazy_import
# test_import_processor.py
from bzrlib import lazy_import
import pytest
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def processor():
    return ImportProcessor(CustomImportReplacer)

def test_instantiation(processor):
    assert isinstance(processor, ImportProcessor)
    assert processor._lazy_import_class == CustomImportReplacer

def test_adding_imports(processor):
    processor.imports['foo'] = (['bzrlib', 'foo'], None, {})
    processor.imports['bar'] = (['bzrlib', 'foo', 'bar'], None, {})
    assert len(processor.imports) == 2
    assert ('foo', (['bzrlib', 'foo'], None, {})) in processor.imports.items()
    assert ('bar', (['bzrlib', 'foo', 'bar'], None, {})) in processor.imports.items()

def test_converting_imports(processor):
    scope = {'baz': None}
    lazy_import(scope, '''
    from bzrlib import (
        foo,
        bar,
        baz,
    )
    ''')
    processor._convert_imports(scope)
    assert 'foo' in scope
    assert 'bar' in scope
    assert 'baz' in scope

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py:4:0: E0401: Unable to import 'bzrlib' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py:10:27: E0602: Undefined variable 'CustomImportReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0.py:14:43: E0602: Undefined variable 'CustomImportReplacer' (undefined-variable)


"""