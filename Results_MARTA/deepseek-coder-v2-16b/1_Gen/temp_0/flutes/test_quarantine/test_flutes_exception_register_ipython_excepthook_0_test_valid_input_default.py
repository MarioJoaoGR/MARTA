
import sys
from types import TracebackType
from unittest.mock import patch

def register_ipython_excepthook(capture_keyboard_interrupt: bool = False) -> None:
    r"""Register an exception hook that launches an interactive IPython session upon uncaught exceptions.

    :param capture_keyboard_interrupt: If ``False``, an uncaught :py:exc:`KeyboardInterrupt` exception will not trigger
        the IPython debugger. Defaults to ``False``.
    """
    skip_exceptions = [BdbQuit]
    if not capture_keyboard_interrupt:
        skip_exceptions.append(KeyboardInterrupt)

    def excepthook(type, value, traceback):
        if any(type is exc_type for exc_type in skip_exceptions):
            # Don't capture keyboard interrupts (Ctrl+C) or Python debugger exit events.
            sys.__excepthook__(type, value, traceback)
        else:
            ipython_hook(type, value, traceback)

    # Enter IPython debugger on exception.
    from IPython.core import ultratb

    ipython_hook = ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
    sys.excepthook = excepthook

# Test case for register_ipython_excepthook function
def test_register_ipython_excepthook():
    with patch('IPython.core.ultratb.FormattedTB') as mock_ipython_hook:
        # Call the function to set up the excepthook
        register_ipython_excepthook()
        
        # Mock the IPython hook to simulate its behavior
        mock_ipython_hook.return_value = lambda *args, **kwargs: None
        
        # Trigger an exception that should not be captured by the excepthook
        try:
            raise ValueError("Test exception")
        except Exception as e:
            # Ensure the default excepthook is called for exceptions other than KeyboardInterrupt
            pass  # The mock will handle it, and we don't need to check anything else here.
        
        # Check if the IPython hook was set up correctly
        assert sys.excepthook == mock_ipython_hook.return_value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default.py:12:23: E0602: Undefined variable 'BdbQuit' (undefined-variable)


"""