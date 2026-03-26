
# Module: flutes.log
import pytest
from multiprocessing_log_handler import MultiprocessingFileHandler as mplh
from pathlib import Path
import logging
import queue
import threading
import multiprocessing as mp

# Fixture to create a temporary log file for testing
@pytest.fixture(scope="module")
def temp_log_file():
    # Create a unique temporary log file name
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile(delete=False, mode='w+t') as tmp:
        yield tmp.name

# Test initialization with default parameters
def test_init_default_parameters(temp_log_file):
    handler = mplh(Path(temp_log_file))
    assert isinstance(handler._handler, logging.FileHandler)
    assert handler._handler.baseFilename == temp_log_file
    assert handler._handler.mode == "a"
    assert isinstance(handler.queue, mp.Queue)
    assert not handler.queue.empty()  # Ensure the queue is initialized and non-empty

# Test initialization with specified mode
def test_init_with_specified_mode(temp_log_file):
    handler = mplh(Path(temp_log_file), mode="w")
    assert isinstance(handler._handler, logging.FileHandler)
    assert handler._handler.baseFilename == temp_log_file
    assert handler._handler.mode == "w"
    assert isinstance(handler.queue, mp.Queue)
    assert not handler.queue.empty()  # Ensure the queue is initialized and non-empty

# Test initialization with custom path
def test_init_with_custom_path():
    temp_path = Path("custom/path/to/logs/app.log")
    handler = mplh(temp_path)
    assert isinstance(handler._handler, logging.FileHandler)
    assert handler._handler.baseFilename == str(temp_path)
    assert handler._handler.mode == "a"
    assert isinstance(handler.queue, mp.Queue)
    assert not handler.queue.empty()  # Ensure the queue is initialized and non-empty

# Test receiving messages from the queue
def test_receive():
    handler = mplh(Path("logs/app.log"))
    msg = "Test log message"
    handler.queue.put(msg)
    
    # Give some time for the thread to process the message (this is a bit hacky and should be improved if possible)
    threading.Event().wait(0.1)
    
    with open(handler._handler.baseFilename, "r") as log_file:
        content = log_file.read()
        assert msg in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler___init___0
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___0.py:4:0: E0401: Unable to import 'multiprocessing_log_handler' (import-error)


"""