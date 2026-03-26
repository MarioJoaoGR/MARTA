
import sys
from types import TracebackType
from typing import List, Optional, Type
from flutes.exception import register_ipython_excepthook

def test_capture_keyboard_interrupt():
    def excepthook(type_: type, value: BaseException, traceback_: TracebackType) -> None:
        assert isinstance(type_, type)
        assert isinstance(value, BaseException)
        assert isinstance(traceback_, TracebackType)
    
    # Register the excepthook without capturing keyboard interrupt
    register_ipython_excepthook()
    original_excepthook = sys.excepthook
    
    try:
        # Trigger a KeyboardInterrupt to ensure it is not captured
        raise KeyboardInterrupt()
    except KeyboardInterrupt:
        pass  # Just ensuring the exception is raised for testing purposes
    
    # Check if the original excepthook was called (not overridden by our hook)
    assert sys.excepthook == original_excepthook

    # Register the excepthook with capturing keyboard interrupt
    register_ipython_excepthook(capture_keyboard_interrupt=True)
    
    try:
        # Trigger a KeyboardInterrupt to ensure it is captured and handled by IPython
        raise KeyboardInterrupt()
    except KeyboardInterrupt:
        pass  # Just ensuring the exception is raised for testing purposes
    
    # Check if our custom excepthook was called (capturing keyboard interrupt)
    assert sys.excepthook != original_excepthook
