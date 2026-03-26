
import sys
from unittest.mock import patch
from IPython.core import ultratb
from flutes.exception import BdbQuit

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

# Test case for register_ipython_excepthook with no capture of KeyboardInterrupt
def test_register_ipython_excepthook_no_capture():
    with patch('sys.excepthook', autospec=True) as mock_excepthook:
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        # Simulate a KeyboardInterrupt to trigger the excepthook
        try:
            raise KeyboardInterrupt()
        except KeyboardInterrupt:
            pass  # Just re-raise it to let the exception propagate

# Test case for register_ipython_excepthook with capture of KeyboardInterrupt
def test_register_ipython_excepthook_capture():
    with patch('sys.excepthook', autospec=True) as mock_excepthook:
        register_ipython_excepthook(capture_keyboard_interrupt=True)
        # Simulate a KeyboardInterrupt to trigger the excepthook
        try:
            raise KeyboardInterrupt()
        except KeyboardInterrupt:
            pass  # Just re-raise it to let the exception propagate
