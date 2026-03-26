
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import multiprocessing
import queue as mpqueue

def test_valid_case():
    # Create a temporary file to write to
    temp_path = Path('test_output.log')
    
    # Initialize the writer with the temporary file path and mode 'a' for append
    writer = MultiprocessingFileWriter(temp_path, mode='a')
    
    # Ensure the queue is initialized correctly
    assert isinstance(writer._queue, mpqueue.Queue)
    
    # Create a function to write messages into the queue
    def write_message():
        writer._queue.put("This is a message to be written to the file.")
    
    # Start a new process to write a message into the queue
    p = multiprocessing.Process(target=write_message)
    p.start()
    p.join()
    
    # Read the content of the temporary file to check if the message was written
    with open(temp_path, 'r') as f:
        content = f.read()
    
    # Assert that the message is in the file content
    assert "This is a message to be written to the file." in content
    
    # Clean up by removing the temporary file
    temp_path.unlink()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___init___0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___0_test_valid_case.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""