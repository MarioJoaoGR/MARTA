
from pytutils.lazy.lazy_import import ScopeReplacer

def test_disallow_proxying():
    # Arrange
    from unittest.mock import patch
    
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        # Act
        disallow_proxying()
        
        # Assert
        assert ScopeReplacer._should_proxy == False, "The _should_proxy attribute should be set to False after calling disallow_proxying."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_0_test_valid_input.py:10:8: E0602: Undefined variable 'disallow_proxying' (undefined-variable)


"""