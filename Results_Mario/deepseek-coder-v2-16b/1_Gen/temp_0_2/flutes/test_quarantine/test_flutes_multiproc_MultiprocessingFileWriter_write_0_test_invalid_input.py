
import pytest
from flutes.multiproc import MultiprocessingFileWriter

def test_invalid_input():
    writer = MultiprocessingFileWriter('output.log')
    
    with pytest.raises(TypeError):
        writer.write(123)  # Passing an integer to simulate invalid input

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        writer = MultiprocessingFileWriter('output.log')
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_invalid_input.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================

Exception in thread Thread-1 (_receive):
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 773, in _receive
    self._file.write(record)
TypeError: write() argument must be str, not int
"""