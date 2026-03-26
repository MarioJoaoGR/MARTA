
import pytest
from flutes.multiproc import MultiprocessingFileWriter
import multiprocessing as mp
import threading

def test_valid_input():
    valid_input = ('example.log', 'a')
    path, mode = valid_input
    writer = MultiprocessingFileWriter(path, mode)
    
    # Ensure the file is opened in the correct mode
    assert writer._file.mode == mode
    
    # Ensure the thread has started and is daemonized
    assert isinstance(writer._thread, threading.Thread)
    assert writer._thread.daemon
    
    # Ensure the queue is initialized correctly
    assert isinstance(writer._queue, mp.Queue)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        valid_input = ('example.log', 'a')
        path, mode = valid_input
        writer = MultiprocessingFileWriter(path, mode)
    
        # Ensure the file is opened in the correct mode
        assert writer._file.mode == mode
    
        # Ensure the thread has started and is daemonized
        assert isinstance(writer._thread, threading.Thread)
        assert writer._thread.daemon
    
        # Ensure the queue is initialized correctly
>       assert isinstance(writer._queue, mp.Queue)
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___0_test_valid_input.py:20: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""