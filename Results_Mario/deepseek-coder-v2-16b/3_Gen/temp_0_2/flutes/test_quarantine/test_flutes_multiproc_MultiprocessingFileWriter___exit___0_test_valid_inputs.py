
import pytest
from multiprocessing import Process, Queue
from pathlib import Path
import time

# Assuming the class is in a module named 'flutes.multiproc'
from flutes.multiproc import MultiprocessingFileWriter

def write_to_file(queue, file_path):
    writer = MultiprocessingFileWriter(file_path)
    while not queue.empty():
        message = queue.get()
        writer._queue.put(message)
    time.sleep(0.1)  # Small delay to allow other processes to write
    writer.__exit__(None, None, None)

@pytest.fixture
def setup_file_and_queue():
    file_path = "test_log.txt"
    queue = Queue()
    yield file_path, queue  # provide the fixture value
    Path(file_path).unlink()  # clean up after test

@pytest.mark.timeout(10)  # Set a timeout for the test to avoid hanging indefinitely
def test_valid_inputs(setup_file_and_queue):
    file_path, queue = setup_file_and_queue
    processes = []
    
    num_processes = 5
    for i in range(num_processes):
        queue.put(f"Message {i}")
    
    for _ in range(num_processes):
        p = Process(target=write_to_file, args=(queue, file_path))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    # Read the content of the file to check if all messages are present
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    expected_messages = {f"Message {i}" for i in range(num_processes)}
    assert set(content.split("\n")) == expected_messages, "Not all messages were written to the file."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""