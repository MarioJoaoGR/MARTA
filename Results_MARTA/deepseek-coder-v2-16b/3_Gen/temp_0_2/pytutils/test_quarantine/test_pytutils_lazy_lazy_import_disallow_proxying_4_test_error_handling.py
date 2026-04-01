
from pytutils.lazy import lazy_import

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

def test_disallow_proxying():
    # Import the necessary module for testing
    from pytutils.lazy import lazy_import
    
    # Call the function to disallow proxying
    disallow_proxying()
    
    # Add your assertions or checks here to verify that the function works as expected
    assert ScopeReplacer._should_proxy == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_4_test_error_handling
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_4_test_error_handling.py:13:4: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_4_test_error_handling.py:23:11: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)


"""