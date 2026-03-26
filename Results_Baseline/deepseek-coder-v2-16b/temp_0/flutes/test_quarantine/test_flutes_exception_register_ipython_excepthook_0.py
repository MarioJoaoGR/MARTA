
import pytest
from flutes.exception import register_ipython_excepthook
import sys
from IPython.core.ultratb import FormattedTB
from bdb import BdbQuit

def test_register_ipython_excepthook_default():
    # Test the default behavior without capturing keyboard interrupt
    register_ipython_excepthook()
    original_excepthook = sys.excepthook
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0.py:15:28: E0001: Parsing failed: 'expected an indented block after 'except' statement on line 15 (Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0, line 15)' (syntax-error)


"""