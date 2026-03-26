
import pytest
from pathlib import Path
import multiprocessing as mp
import threading
from unittest.mock import patch

# Import the function from the module
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def setup_writer():
    writer = MultiprocessingFileWriter(Path('testfile.log'))
    yield writer
    # Clean up by closing the file and joining the thread (if necessary)
    writer._thread.join()
    writer._file.close()

@pytest.mark.parametrize("message", ["Hello, world!", "This is a test message.", "Another log entry."])
def test_write(setup_writer, message):
    setup_writer.write(message)
    with open('testfile.log', 'r') as f:
        content = f.read()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""