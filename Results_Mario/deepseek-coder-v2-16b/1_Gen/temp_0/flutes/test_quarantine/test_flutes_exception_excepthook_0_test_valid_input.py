
import sys
from IPython.core.hooks import ExceptionHook
from flutes.exception import excepthook

def test_valid_input():
    skip_exceptions = (KeyboardInterrupt,)
    ipython_hook = ExceptionHook()

    def mock_excepthook(type, value, traceback):
        if any(type is exc_type for exc_type in skip_exceptions):
            sys.__excepthook__(type, value, traceback)
        else:
            ipython_hook(type, value, traceback)
    
    # Set the custom excepthook as the new default exception handler
    sys.excepthook = mock_excepthook

    try:
        1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        pass  # We expect this to be caught by the custom excepthook

    # Reset the original excepthook for other tests
    sys.excepthook = sys.__excepthook__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_excepthook_0_test_valid_input
flutes/Test4DT_tests/test_flutes_exception_excepthook_0_test_valid_input.py:3:0: E0611: No name 'ExceptionHook' in module 'IPython.core.hooks' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception_excepthook_0_test_valid_input.py:4:0: E0611: No name 'excepthook' in module 'flutes.exception' (no-name-in-module)


"""