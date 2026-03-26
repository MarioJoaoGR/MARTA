
import sys
from unittest.mock import patch, MagicMock
from flutes.exception import BdbQuit
from your_module import register_ipython_excepthook

def test_register_ipython_excepthook():
    with patch('your_module.sys.excepthook', new=MagicMock()) as mock_excepthook:
        # Test without capturing KeyboardInterrupt
        register_ipython_excepthook()
        _, value, _ = sys.exc_info()
        assert not isinstance(value, KeyboardInterrupt)
        mock_excepthook.assert_called_once()

        # Reset the excepthook for the next test
        mock_excepthook.reset_mock()

        # Test capturing KeyboardInterrupt
        register_ipython_excepthook(capture_keyboard_interrupt=True)
        _, value, _ = sys.exc_info()
        assert not isinstance(value, KeyboardInterrupt)
        mock_excepthook.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_valid_input_capture_keyboard_interrupt
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_capture_keyboard_interrupt.py:5:0: E0401: Unable to import 'your_module' (import-error)


"""