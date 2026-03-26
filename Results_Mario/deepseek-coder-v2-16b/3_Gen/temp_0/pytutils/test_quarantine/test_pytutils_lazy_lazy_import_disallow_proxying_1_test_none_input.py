
from pytutils.lazy.lazy_import import ScopeReplacer

def test_none_input():
    """Test that disallowing proxying works correctly."""
    # Initial state should be True, as this is the default value
    assert ScopeReplacer._should_proxy == True
    
    # Call the function to set _should_proxy to False
    disallow_proxying()
    
    # After calling the function, _should_proxy should be False
    assert ScopeReplacer._should_proxy == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_1_test_none_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_1_test_none_input.py:10:4: E0602: Undefined variable 'disallow_proxying' (undefined-variable)


"""