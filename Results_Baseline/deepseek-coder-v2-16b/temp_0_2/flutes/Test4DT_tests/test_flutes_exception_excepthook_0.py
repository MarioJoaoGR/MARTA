
import sys
from IPython.core import ultratb

# Assuming skip_exceptions is defined somewhere in the module
skip_exceptions = (KeyboardInterrupt,)  # List of exceptions to skip

def ipython_hook(exc_type, exc_value, tb):
    print("IPython hook triggered with exception:", exc_value)

def excepthook(type, value, traceback):
    if any(type is exc_type for exc_type in skip_exceptions):
        sys.__excepthook__(type, value, traceback)
    else:
        ipython_hook(type, value, traceback)

# Set the custom excepthook for the application
sys.excepthook = excepthook

def test_standard_exception():
    try:
        1 / 0
    except Exception as e:
        sys.excepthook(e.__class__, e, e.__traceback__)