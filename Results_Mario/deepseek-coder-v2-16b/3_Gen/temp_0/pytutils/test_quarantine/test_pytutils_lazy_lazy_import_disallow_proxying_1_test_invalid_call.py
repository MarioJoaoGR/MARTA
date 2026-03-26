
from pytutils.lazy.lazy_import import ScopeReplacer

def test_invalid_call():
    """Test that disallows proxying of lazy imports."""
    # Before calling disallow_proxying, ensure _should_proxy is True by default
    assert getattr(ScopeReplacer, '_should_proxy', None) is not False
    
    # Call the function to set _should_proxy to False
    disallow_proxying()
    
    # After calling disallow_proxying, ensure _should_proxy is now False
    assert ScopeReplacer._should_proxy == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_1_test_invalid_call
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_1_test_invalid_call.py:10:4: E0602: Undefined variable 'disallow_proxying' (undefined-variable)


"""