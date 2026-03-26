
import pytest
from flutes.multiproc import MultiprocessingFileWriter

def test_valid_inputs():
    path = "test.txt"
    writer = MultiprocessingFileWriter(path)
    
    assert isinstance(writer._file, file), "Expected _file to be a file instance."
    assert isinstance(writer._queue, mp.Queue), "Expected _queue to be an instance of mp.Queue."
    assert writer._thread.is_alive(), "Expected the thread to be running."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___init___0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___0_test_valid_inputs.py:9:36: E0602: Undefined variable 'file' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___0_test_valid_inputs.py:10:37: E0602: Undefined variable 'mp' (undefined-variable)

"""