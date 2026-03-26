
import pytest
from flutes.multiproc import MultiprocessingFileWriter

def test_invalid_inputs():
    with pytest.raises(TypeError):
        MultiprocessingFileWriter(42)  # Passing an integer instead of a string

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
>           MultiprocessingFileWriter(42)  # Passing an integer instead of a string

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_inputs.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f9cbf0c6990>
path = 42, mode = 'a'

    def __init__(self, path: PathType, mode: str = "a"):
>       self._file = open(path, mode)
E       OSError: [Errno 9] Bad file descriptor

flutes/flutes/multiproc.py:752: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter__receive_3_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""