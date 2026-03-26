
import sys
from typing import List, Type
from IPython.core.debugger import BdbQuit

def register_ipython_excepthook(capture_keyboard_interrupt: bool = False) -> None:
    r"""Register an exception hook that launches an interactive IPython session upon uncaught exceptions.

    :param capture_keyboard_interrupt: If ``False``, an uncaught :py:exc:`KeyboardInterrupt` exception will not trigger
        the IPython debugger. Defaults to ``False``.
    """
    skip_exceptions: List[Type[BaseException]] = [BdbQuit]
    if not capture_keyboard_interrupt:
        skip_exceptions.append(KeyboardInterrupt)

    def excepthook(type, value, traceback):
        if any(type is exc_type for exc_type in skip_exceptions):
            # Don't capture keyboard interrupts (Ctrl+C) or Python debugger exit events.
            sys.__excepthook__(type, value, traceback)
        else:
            from IPython.core import ultratb
            ipython_hook = ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
            ipython_hook(type, value, traceback)

    # Enter IPython debugger on exception.
    sys.excepthook = excepthook

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_capture_keyboard_interrupt
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_capture_keyboard_interrupt.py:4:0: E0611: No name 'BdbQuit' in module 'IPython.core.debugger' (no-name-in-module)


"""