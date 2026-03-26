
import sys
from types import Type
from unittest.mock import patch
from IPython.core import ultratb
from flutes.exception import register_ipython_excepthook

def test_register_ipython_excepthook():
    with patch('IPython.core.ultratb.FormattedTB', return_value=None) as mock_ipython_hook:
        # Test without capturing KeyboardInterrupt
        register_ipython_excepthook()
        assert sys.excepthook == mock_ipython_hook.return_value.__call__
        
        # Test with capturing KeyboardInterrupt
        register_ipython_excepthook(capture_keyboard_interrupt=True)
        assert sys.excepthook == mock_ipython_hook.return_value.__call__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_invalid_inputs.py:3:0: E0611: No name 'Type' in module 'types' (no-name-in-module)


"""