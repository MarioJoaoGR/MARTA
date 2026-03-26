
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from bzrlib import lazy_import
import pytest

@pytest.fixture(scope="module")
def processor():
    from pytutils.lazy.lazy_import import ImportProcessor
    return ImportProcessor()

@pytest.fixture(scope="module")
def scope():
    return globals()

@pytest.mark.parametrize("text, expected", [
    ("""
     from bzrlib import (
         foo,
         bar,
         baz,
     )
     import bzrlib.branch
     import bzrlib.transport
     """, None),
    ("from bzrlib import foo", "foo"),
    ("import bzrlib.branch", "bzrlib.branch"),
])
def test_process_imports(processor, scope, text, expected):
    processor.process_imports(scope, text)
    if expected:
        assert hasattr(scope[expected], '__lazy__')
    else:
        for name in ['foo', 'bar', 'baz', 'bzrlib.branch', 'bzrlib.transport']:
            assert hasattr(scope[name], '__lazy__')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0.py:4:0: E0401: Unable to import 'bzrlib' (import-error)


"""