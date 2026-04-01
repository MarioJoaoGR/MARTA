
import pytest
from pathlib import Path
import logging
import multiprocessing as mp
import threading
from flutes.log import MultiprocessingFileHandler

@pytest.mark.parametrize("path", [None, 123, b"bytes_path"])
def test_invalid_inputs(path):
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___2_test_invalid_inputs.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_inputs[bytes_path] ________________________

path = b'bytes_path'

    @pytest.mark.parametrize("path", [None, 123, b"bytes_path"])
    def test_invalid_inputs(path):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___2_test_invalid_inputs.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler___init___2_test_invalid_inputs.py::test_invalid_inputs[bytes_path]
========================= 1 failed, 2 passed in 0.10s ==========================
"""