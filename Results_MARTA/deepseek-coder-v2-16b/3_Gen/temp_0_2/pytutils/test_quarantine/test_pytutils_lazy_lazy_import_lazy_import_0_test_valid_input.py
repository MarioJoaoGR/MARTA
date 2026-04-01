
from pytutils.lazy import lazy_import
import pytest

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
    
    result = lazy_import(scope, text)
    
    assert 'foo' in result['bzrlib']
    assert 'bar' in result['bzrlib']
    assert 'baz' in result['bzrlib']
    assert 'branch' in result['bzrlib']
    assert 'transport' in result['bzrlib']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_lazy_import_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_lazy_import_0_test_valid_input.py:17:13: E1102: lazy_import is not callable (not-callable)


"""