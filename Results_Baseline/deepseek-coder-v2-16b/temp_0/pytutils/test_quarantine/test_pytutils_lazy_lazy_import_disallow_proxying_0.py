
# Module: pytutils.lazy.lazy_import
# Import the function correctly from its module
from pytutils.lazy.lazy_import import disallow_proxying

def test_disallow_proxying():
    # Initially, assume _should_proxy is True (default behavior)
    assert getattr(ScopeReplacer, '_should_proxy', True) == True
    
    # Call the function to set _should_proxy to False
    disallow_proxying()
    
    # After calling the function, _should_proxy should be False
    assert getattr(ScopeReplacer, '_should_proxy', False) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_0
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_0.py:8:19: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_0.py:14:19: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)


"""