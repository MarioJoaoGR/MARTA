
import pytest
from multiprocessing_logging_handler import MultiprocessingFileHandler
import logging
import threading
import multiprocessing as mp
from pathlib import Path

def test_invalid_input():
    with pytest.raises(TypeError):
        # Create an instance of MultiprocessingFileHandler
        handler = MultiprocessingFileHandler(Path("logfile.log"))
        
        # Try to send a non-string value, such as a number or object
        handler.send(123)  # This should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_send_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_1_test_invalid_input.py:3:0: E0401: Unable to import 'multiprocessing_logging_handler' (import-error)


"""