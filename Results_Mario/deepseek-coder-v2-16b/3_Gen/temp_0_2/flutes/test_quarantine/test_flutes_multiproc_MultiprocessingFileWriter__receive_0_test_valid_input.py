
import pytest
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import multiprocessing as mp
import io

@pytest.fixture(scope="module")
def setup():
    path = "test_log.txt"
    writer = MultiprocessingFileWriter(path)
    yield writer
    # Clean up the file after the test
    with open(path, 'r+') as f:
        f.truncate(0)

def test_valid_input(setup):
    writer = setup
    msg1 = "Hello, world!"
    msg2 = "This is a test."
    
    # Add messages to the queue from multiple processes
    mp_queue = writer._queue
    p1 = mp.Process(target=mp_queue.put, args=(msg1,))
    p2 = mp.Process(target=mp_queue.put, args=(msg2,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    # Give some time for the thread to process the queue (this is a crude way to wait)
    threading.Event().wait(0.1)
    
    # Read the file and check if both messages are present
    with open("test_log.txt", "r") as f:
        content = f.read()
        assert msg1 in content
        assert msg2 in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter__receive_0_test_valid_input
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_0_test_valid_input.py:3:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""