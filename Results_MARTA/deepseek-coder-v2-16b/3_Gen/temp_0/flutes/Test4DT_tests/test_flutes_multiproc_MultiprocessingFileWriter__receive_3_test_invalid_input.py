
import pytest
from flutes.multiproc import MultiprocessingFileWriter
import multiprocessing as mp
import threading

@pytest.fixture
def setup_writer():
    writer = MultiprocessingFileWriter("dummy_path", mode="a")
    # Mock the queue to contain non-string data
    writer._queue = mp.Queue(-1)  # Reset the queue for fresh testing
    return writer

def test_invalid_input(setup_writer):
    setup_writer._queue.put(12345)  # Insert an integer into the queue, which should raise a TypeError
    
    with pytest.raises(TypeError):
        setup_writer._receive()  # Call _receive to trigger the error
