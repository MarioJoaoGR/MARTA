
import sys
from unittest.mock import patch, MagicMock
from flutes.exception import register_ipython_excepthook

def test_register_ipython_excepthook():
    with patch('flutes.exception.ultratb.FormattedTB') as mock_formattetb:
        # Create a mock instance of FormattedTB to simulate IPython debugger behavior
        mock_instance = MagicMock()
        mock_formattetb.return_value = mock_instance
        
        # Call the function without any parameters
        register_ipython_excepthook()
        
        # Check if sys.excepthook is set to our custom excepthook
        assert sys.excepthook == mock_formattetb.return_value.__call__
        
        # Now call the function with capture_keyboard_interrupt=True
        register_ipython_excepthook(capture_keyboard_interrupt=True)
        
        # Check if skip_exceptions includes KeyboardInterrupt
        from flutes.exception import skip_exceptions
        assert KeyboardInterrupt in skip_exceptions

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default.py:22:8: E0611: No name 'skip_exceptions' in module 'flutes.exception' (no-name-in-module)


"""