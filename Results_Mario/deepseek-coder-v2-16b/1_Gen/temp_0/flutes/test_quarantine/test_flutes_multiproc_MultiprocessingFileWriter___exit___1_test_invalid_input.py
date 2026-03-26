
import pytest
from flutes.multiproc import MultiprocessingFileWriter
from pathlib import Path

def test_invalid_input():
    with pytest.raises(TypeError):
        MultiprocessingFileWriter("not_a_path", "invalid_mode")

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           MultiprocessingFileWriter("not_a_path", "invalid_mode")

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___1_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f2bf82f7bd0>
path = 'not_a_path', mode = 'invalid_mode'

    def __init__(self, path: PathType, mode: str = "a"):
>       self._file = open(path, mode)
E       ValueError: invalid mode: 'invalid_mode'

flutes/flutes/multiproc.py:752: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""