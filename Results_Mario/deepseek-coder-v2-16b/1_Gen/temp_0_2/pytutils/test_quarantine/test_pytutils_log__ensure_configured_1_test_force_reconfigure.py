
import pytest
from unittest.mock import patch
from pytutils.log import _ensure_configured, configure

@pytest.fixture(autouse=True)
def reset_configuration():
    # Reset the _CONFIGURED flag before each test to ensure a clean state
    if not hasattr(_ensure_configured, "_has_configured"):
        setattr(_ensure_configured, "_has_configured", [False])

@pytest.mark.parametrize("initial_state, expected_result", [
    (False, True),  # If not configured initially, it should be configured after the call
    (True, False)   # If already configured, no action should be taken
])
def test_force_reconfigure(initial_state, expected_result):
    if initial_state:
        setattr(_ensure_configured, "_has_configured", [True])
    
    with patch('pytutils.log.configure') as mock_configure:
        _ensure_configured()
        
        if not initial_state:
            assert mock_configure.called
            assert _ensure_configured._has_configured[-1] == expected_result
        else:
            assert not mock_configure.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_log__ensure_configured_1_test_force_reconfigure
pytutils/Test4DT_tests/test_pytutils_log__ensure_configured_1_test_force_reconfigure.py:25:19: E1101: Function '_ensure_configured' has no '_has_configured' member (no-member)


"""