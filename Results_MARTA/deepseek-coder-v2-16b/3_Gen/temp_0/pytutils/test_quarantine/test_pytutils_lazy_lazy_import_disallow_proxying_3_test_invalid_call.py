
from pytutils.lazy.lazy_import import ScopeReplacer

def test_invalid_call():
    # Arrange
    original_should_proxy = ScopeReplacer._should_proxy
    
    # Act
    disallow_proxying()
    
    # Assert
    assert not ScopeReplacer._should_proxy, "The _should_proxy attribute should be set to False after calling disallow_proxying."
    
    # Restore the original state for other tests
    ScopeReplacer._should_proxy = original_should_proxy

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_3_test_invalid_call
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_3_test_invalid_call.py:9:4: E0602: Undefined variable 'disallow_proxying' (undefined-variable)


"""