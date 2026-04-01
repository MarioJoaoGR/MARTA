
from pytutils.lazy import lazy_import

def test_valid_input():
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
    
    lazy_import(scope, text)
    
    assert 'foo' in scope
    assert 'bar' in scope
    assert 'baz' in scope
    assert 'bzrlib' in scope

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_lazy_import_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_lazy_import_0_test_valid_input.py:16:4: E1102: lazy_import is not callable (not-callable)


"""