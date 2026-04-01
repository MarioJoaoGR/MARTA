
import pytest
from flutes.multiproc import MultiprocessingFileWriter
import multiprocessing as mp
import threading

@pytest.fixture(scope="function")
def setup_writer():
    writer = MultiprocessingFileWriter('test_log.txt')
    yield writer
    # Clean up the file after the test
    with open('test_log.txt', 'w') as f:
        f.truncate(0)

def test_valid_inputs(setup_writer):
    writer = setup_writer
    message1 = "Message 1\n"
    message2 = "Message 2\n"
    
    # Put messages in the queue
    writer._queue.put(message1)
    writer._queue.put(message2)
    
    # Allow time for the thread to process the queue
    threading.Event().wait(0.1)
    
    # Read the contents of the file to check if messages were written correctly
    with open('test_log.txt', 'r') as f:
        content = f.read()
        
    assert message1 in content
    assert message2 in content

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

setup_writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f9dff708890>

    def test_valid_inputs(setup_writer):
        writer = setup_writer
        message1 = "Message 1\n"
        message2 = "Message 2\n"
    
        # Put messages in the queue
        writer._queue.put(message1)
        writer._queue.put(message2)
    
        # Allow time for the thread to process the queue
        threading.Event().wait(0.1)
    
        # Read the contents of the file to check if messages were written correctly
        with open('test_log.txt', 'r') as f:
            content = f.read()
    
>       assert message1 in content
E       AssertionError: assert 'Message 1\n' in ''

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_valid_inputs.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.21s ===============================
"""