
import pytest
from multiprocessing_file_writer import MultiprocessingFileWriter
import threading
import queue as mp_queue

def test_edge_case_none():
    with pytest.raises(TypeError):
        writer = MultiprocessingFileWriter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter__receive_0_test_edge_case_none
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_0_test_edge_case_none.py:3:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""