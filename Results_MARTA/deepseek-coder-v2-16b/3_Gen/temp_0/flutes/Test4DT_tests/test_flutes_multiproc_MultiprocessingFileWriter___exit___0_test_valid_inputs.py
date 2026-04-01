
import pytest
from unittest.mock import MagicMock
from flutes.multiproc import MultiprocessingFileWriter
import multiprocessing as mp
from pathlib import Path

@pytest.fixture
def setup_writer():
    queue = mp.Queue()
    writer = MultiprocessingFileWriter("example.log", mode="a")
    for i in range(10):
        queue.put(f"Log entry {i}")
    return writer, queue

def test_valid_inputs(setup_writer):
    writer, queue = setup_writer
    
    # Mock the necessary methods and attributes to simulate exiting context
    writer._thread = MagicMock()
    writer._file = MagicMock()
    
    # Call __exit__ method
    writer.__exit__(None, None, None)
    
    # Assertions to verify expected behavior
    assert writer._thread.join.called
    assert writer._file.close.called
