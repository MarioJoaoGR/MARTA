
import pytest
from pathlib import Path
import threading
import queue
import multiprocessing as mp
import time

# Assuming the class is defined in a module named 'flutes.multiproc'
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture(scope="function")
def setup_writer():
    # Create a temporary file for testing
    temp_file = Path("test_output.log")
    if temp_file.exists():
        temp_file.unlink()  # Remove the existing file if it exists
    
    writer = MultiprocessingFileWriter(temp_file, mode="a")
    yield writer  # Provide the fixture value
    writer._thread.join()  # Ensure the thread is joined after the test
    temp_file.unlink()  # Clean up the temporary file

def test_valid_inputs(setup_writer):
    writer = setup_writer
    
    def write_to_queue(q, msg):
        q.put(msg)
    
    # Create a queue and start writing to it from multiple processes
    queue1 = mp.Queue()
    queue2 = mp.Queue()
    
    p1 = mp.Process(target=write_to_queue, args=(queue1, "Hello, "))
    p2 = mp.Process(target=write_to_queue, args=(queue2, "World!"))
    
    p1.start()
    p2.start()
    
    # Let the processes run for a short while to fill up their queues
    time.sleep(0.5)
    
    writer._receive()  # Trigger the receive method in the thread
    
    # Wait for both processes to finish and close their queues
    p1.join()
    p2.join()
    
    # Read the contents of the file after both processes have finished writing
    with open(writer._file.name, "r") as f:
        content = f.read()
    
    assert "Hello, " in content
    assert "World!" in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""