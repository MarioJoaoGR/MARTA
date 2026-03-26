
import sys
from unittest.mock import patch
from IPython.core.ultratb import FormattedTB
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

    ipython_hook = FormattedTB(mode='Context', color_scheme='Linux', call_pdb=1)
    sys.excepthook = excepthook

# Test case for register_ipython_excepthook with capture_keyboard_interrupt set to True and False
def test_register_ipython_excepthook():
    with patch('sys.excepthook', autospec=True) as mock_excepthook:
        # Test when capture_keyboard_interrupt is False
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        assert sys.excepthook == mock_excepthook.return_value
        
        # Test when capture_keyboard_interrupt is True
        register_ipython_excepthook(capture_keyboard_interrupt=True)
        assert sys.excepthook == mock_excepthook.return_value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
_______________________ test_register_ipython_excepthook _______________________

    def test_register_ipython_excepthook():
        with patch('sys.excepthook', autospec=True) as mock_excepthook:
            # Test when capture_keyboard_interrupt is False
            register_ipython_excepthook(capture_keyboard_interrupt=False)
>           assert sys.excepthook == mock_excepthook.return_value
E           AssertionError: assert <function register_ipython_excepthook.<locals>.excepthook at 0x7f5dcddf4180> == <MagicMock name='excepthook()' id='140040863064848'>
E            +  where <function register_ipython_excepthook.<locals>.excepthook at 0x7f5dcddf4180> = sys.excepthook
E            +  and   <MagicMock name='excepthook()' id='140040863064848'> = <MagicMock name='excepthook' spec='builtin_function_or_method' id='140040862573328'>.return_value

flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_invalid_input_none.py:35: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_invalid_input_none.py::test_register_ipython_excepthook
============================== 1 failed in 0.54s ===============================
"""