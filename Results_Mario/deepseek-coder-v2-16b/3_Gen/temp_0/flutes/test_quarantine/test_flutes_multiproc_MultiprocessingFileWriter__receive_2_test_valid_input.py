
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import multiprocessing
import os

@pytest.fixture(scope="function")
def setup():
    writer = MultiprocessingFileWriter(Path('test.log'))
    yield writer
    # Clean up the file after the test
    if os.path.exists('test.log'):
        os.remove('test.log')

def test_valid_input(setup):
    writer = setup
    
    def write_message():
        writer._queue.put("This is a valid message.")
    
    # Start a new process to put the message into the queue
    p = multiprocessing.Process(target=write_message)
    p.start()
    p.join()
    
    # Ensure the message is written to the file
    with open('test.log', 'r') as f:
        content = f.read()
        assert "This is a valid message." in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter__receive_2_test_valid_input
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_2_test_valid_input.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""