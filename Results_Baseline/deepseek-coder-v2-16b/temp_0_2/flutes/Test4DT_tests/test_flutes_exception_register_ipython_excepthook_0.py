# Module: flutes.exception
import pytest
from flutes.exception import register_ipython_excepthook
import sys
from IPython.core import ultratb
from bdb import BdbQuit

# Test default usage without capturing KeyboardInterrupt
def test_default_usage():
    try:
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        raise Exception("Test exception")
    except Exception as e:
        assert str(e) == "Test exception"

# Test capturing KeyboardInterrupt
def test_capturing_keyboard_interrupt():
    with pytest.raises(KeyboardInterrupt):
        register_ipython_excepthook()
        raise KeyboardInterrupt("Test keyboard interrupt")

# Test if the excepthook is correctly set up
def test_custom_excepthook():
    original_excepthook = sys.excepthook
    try:
        register_ipython_excepthook()
        # Trigger an exception to see if the custom excepthook is called
        raise Exception("Test exception")
    except Exception as e:
        assert str(e) == "Test exception"
    finally:
        sys.excepthook = original_excepthook

# Test that KeyboardInterrupt is not captured when capture_keyboard_interrupt is False
def test_no_capture_keyboard_interrupt():
    with pytest.raises(KeyboardInterrupt):
        register_ipython_excepthook(capture_keyboard_interrupt=False)
        raise KeyboardInterrupt("Test keyboard interrupt")
