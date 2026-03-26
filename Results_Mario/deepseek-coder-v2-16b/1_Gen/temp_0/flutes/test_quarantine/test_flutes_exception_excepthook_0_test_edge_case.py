
import sys
from IPython.core.hooks import ExceptionHook

# Define the exceptions to skip
skip_exceptions = (KeyboardInterrupt,)

def excepthook(type, value, traceback):
    if any(type is exc_type for exc_type in skip_exceptions):
        # Don't capture keyboard interrupts (Ctrl+C) or Python debugger exit events.
        sys.__excepthook__(type, value, traceback)
    else:
        ipython_hook = ExceptionHook()  # Initialize your IPython hook
        ipython_hook(type, value, traceback)

# Set the custom excepthook as the new default exception handler
sys.excepthook = excepthook

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_excepthook_0_test_edge_case
flutes/Test4DT_tests/test_flutes_exception_excepthook_0_test_edge_case.py:3:0: E0611: No name 'ExceptionHook' in module 'IPython.core.hooks' (no-name-in-module)


"""