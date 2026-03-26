
from pytutils.lazy.lazy_import import ScopeReplacer

def test_invalid_call():
    # Arrange
    original_proxy_state = ScopeReplacer._should_proxy
    
    try:
        # Act
        disallow_proxying()
        
        # Assert
        assert not ScopeReplacer._should_proxy, "Expected _should_proxy to be set to False after calling disallow_proxying"
    finally:
        # Teardown: Reset the original state for other tests
        ScopeReplacer._should_proxy = original_proxy_state

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_0_test_invalid_call
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_0_test_invalid_call.py:10:8: E0602: Undefined variable 'disallow_proxying' (undefined-variable)


"""