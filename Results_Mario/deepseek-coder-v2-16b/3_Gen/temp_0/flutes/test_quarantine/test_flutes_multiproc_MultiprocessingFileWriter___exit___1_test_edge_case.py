
import pytest
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import queue
import os
import multiprocessing

@pytest.fixture(scope="function")
def writer():
    path = "test_output.log"
    w = MultiprocessingFileWriter(path)
    yield w
    # Ensure the thread and file are properly closed after the test
    if os.path.exists(path):
        os.remove(path)

def test_multiprocessing_file_writer_exits_gracefully(writer):
    q = writer._queue  # Accessing the queue to simulate adding messages
    
    def write_message():
        q.put("Test message")
    
    p = multiprocessing.Process(target=write_message)
    p.start()
    p.join()
    
    assert os.path.exists("test_output.log")
    with open("test_output.log", "r") as f:
        content = f.read()
        assert "Test message" in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___exit___1_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___1_test_edge_case.py:3:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""