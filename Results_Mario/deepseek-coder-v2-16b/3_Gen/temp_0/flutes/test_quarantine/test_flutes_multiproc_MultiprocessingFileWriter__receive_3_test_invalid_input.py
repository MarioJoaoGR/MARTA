
import pytest
from pathlib import Path
from flutes.multiproc import MultiprocessingFileWriter  # Adjust the import according to your actual structure
import multiprocessing

@pytest.fixture
def setup_writer():
    return MultiprocessingFileWriter(Path('testfile.log'))

def test_invalid_input(setup_writer):
    writer = setup_writer
    
    # Test that the class can handle invalid input gracefully, e.g., non-string data in the queue
    with pytest.raises(TypeError):  # Expecting a TypeError since non-string data cannot be written to a file
        writer._queue.put(12345)  # Trying to put an integer which is not allowed
    
    # Ensure that no data was actually written to the file (this part assumes some form of logging or error handling in _receive method)
    with open('testfile.log', 'r') as f:
        content = f.read()
        assert "12345" not in content  # Check if the integer was logged or ignored

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

setup_writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f202e01c950>

    def test_invalid_input(setup_writer):
        writer = setup_writer
    
        # Test that the class can handle invalid input gracefully, e.g., non-string data in the queue
>       with pytest.raises(TypeError):  # Expecting a TypeError since non-string data cannot be written to a file
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_input.py:15: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_input.py::test_invalid_input
  /usr/local/lib/python3.11/site-packages/_pytest/threadexception.py:82: PytestUnhandledThreadExceptionWarning: Exception in thread Thread-1 (_receive)
  
  Traceback (most recent call last):
    File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
      self.run()
    File "/usr/local/lib/python3.11/threading.py", line 982, in run
      self._target(*self._args, **self._kwargs)
    File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 773, in _receive
      self._file.write(record)
  TypeError: write() argument must be str, not int
  
    warnings.warn(pytest.PytestUnhandledThreadExceptionWarning(msg))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_input.py::test_invalid_input
========================= 1 failed, 1 warning in 0.11s =========================
"""