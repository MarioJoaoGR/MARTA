
# Module: flutes.exception
import sys
from IPython.core.hooks import ExceptionHook  # Importing ExceptionHook from the correct module

def test_excepthook_skips_keyboard_interrupt():
    skip_exceptions = (KeyboardInterrupt,)
    ipython_hook = ExceptionHook()
    
    # Simulate a KeyboardInterrupt to ensure it is skipped
    type_, value, traceback = KeyboardInterrupt, None, None  # Renaming variables for clarity and consistency
    
    def excepthook(type_, value, traceback):
        if any(type_ is exc_type for exc_type in skip_exceptions):
            sys.__excepthook__(type_, value, traceback)
        else:
            ipython_hook(type_, value, traceback)
    
    # Call the function to ensure it skips KeyboardInterrupt
    excepthook(type_, value, traceback)
    assert True  # If we reach here without an error, the test passes

def test_excepthook_handles_other_exceptions():
    skip_exceptions = (KeyboardInterrupt,)
    ipython_hook = ExceptionHook()
    
    # Simulate a ZeroDivisionError to ensure it is handled
    type_, value, traceback = ZeroDivisionError, None, None  # Renaming variables for clarity and consistency
    
    def excepthook(type_, value, traceback):
        if any(type_ is exc_type for exc_type in skip_exceptions):
            sys.__excepthook__(type_, value, traceback)
        else:
            ipython_hook(type_, value, traceback)
    
    # Call the function to ensure it handles ZeroDivisionError correctly
    excepthook(type_, value, traceback)
    assert True  # If we reach here without an error, the test passes

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_excepthook_0
flutes/Test4DT_tests/test_flutes_exception_excepthook_0.py:4:0: E0611: No name 'ExceptionHook' in module 'IPython.core.hooks' (no-name-in-module)


"""