
from pytutils.lazy import lazy_import, ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_1_test_error_handling
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_1_test_error_handling.py:2:0: E0611: No name 'ScopeReplacer' in module 'pytutils.lazy' (no-name-in-module)


"""