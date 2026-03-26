
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter
import multiprocessing as mp
import threading

@pytest.fixture
def setup_writer():
    writer = MultiprocessingFileWriter(Path('output.log'))
    yield writer
    # Clean up the queue and thread to ensure no residual writes occur after the test
    writer._queue.put(None)  # Signal the thread to stop
    writer._thread.join()     # Wait for the thread to finish
    writer._file.close()      # Close the file handle

def test_invalid_input(setup_writer):
    writer = setup_writer
    with pytest.raises(TypeError):
        writer._receive("invalid input")  # This should raise a TypeError due to invalid argument type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter__receive_6_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_6_test_invalid_input.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""