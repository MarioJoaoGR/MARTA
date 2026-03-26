
# Module: pytutils.lazy.lazy_import
# test_lazy_import.py
from bzrlib import lazy_import
import pytest

@pytest.fixture(scope="module")
def processor():
    from pytutils.lazy.lazy_import import ImportProcessor
    return ImportProcessor()

@pytest.mark.parametrize("text, expected", [
    ("""
    from bzrlib import (
        foo,
        bar,
        baz,
    )
    import bzrlib.branch
    import bzrlib.transport
    """, {}),
    ("from bzrlib import foo", {"foo": None}),
    ("import bzrlib.branch", {"bzrlib.branch": None}),
])
def test_process_imports(processor, text, expected):
    scope = {}
    processor.process_imports(scope, text)
    assert set(processor.imports.keys()) == set(expected.keys())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor___init___0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor___init___0.py:4:0: E0401: Unable to import 'bzrlib' (import-error)


"""