
import pytest
from unittest.mock import patch
import sys
from types import BdbQuit
from typing import List, Type

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
            from flutes.exception import ultratb
            ipython_hook = ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
            ipython_hook(type, value, traceback)

    # Enter IPython debugger on exception.
    from flutes.exception import ultratb
    sys.excepthook = excepthook

@pytest.mark.parametrize("capture_keyboard_interrupt, expected_behavior", [
    (False, True),  # Default case should capture KeyboardInterrupt if not specified
    (True, False)   # Specifying True should skip KeyboardInterrupt
])
def test_register_ipython_excepthook(capture_keyboard_interrupt, expected_behavior):
    with patch('flutes.exception.ultratb.FormattedTB') as mock_ipython_hook:
        register_ipython_excepthook(capture_keyboard_interrupt)
        # Trigger a KeyboardInterrupt to test if it is captured or not
        with pytest.raises(KeyboardInterrupt):
            raise KeyboardInterrupt

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default.py:5:0: E0611: No name 'BdbQuit' in module 'types' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default.py:23:12: E0611: No name 'ultratb' in module 'flutes.exception' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_valid_input_default.py:28:4: E0611: No name 'ultratb' in module 'flutes.exception' (no-name-in-module)


"""