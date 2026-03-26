
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import multiprocessing

@pytest.fixture(scope="module")
def writer():
    return MultiprocessingFileWriter(Path('output.log'))

def test_none_input(writer):
    with pytest.raises(TypeError):
        writer._queue.put(None)

def test_empty_string_input(writer):
    writer._queue.put("")
    # Give some time for the thread to process the queue (this is a bit hacky and should be improved if possible)
    threading.Event().wait(0.1)
    writer._file.seek(0, 0)
    assert writer._file.read() == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter__receive_5_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_5_test_edge_case.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""