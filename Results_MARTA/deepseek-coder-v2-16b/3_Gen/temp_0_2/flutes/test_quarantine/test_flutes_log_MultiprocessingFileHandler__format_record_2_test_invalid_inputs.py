
import pytest
from pathlib import Path
import multiprocessing as mp
import logging
import threading
from flutes.log import MultiprocessingFileHandler

@pytest.mark.parametrize("path", [Path('test_logfile.log'), 'invalid_path'])
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
collected 2 items

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_invalid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[path0] __________________________

path = PosixPath('test_logfile.log')

    @pytest.mark.parametrize("path", [Path('test_logfile.log'), 'invalid_path'])
    def test_invalid_inputs(path):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_invalid_inputs.py:11: Failed
______________________ test_invalid_inputs[invalid_path] _______________________

path = 'invalid_path'

    @pytest.mark.parametrize("path", [Path('test_logfile.log'), 'invalid_path'])
    def test_invalid_inputs(path):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_invalid_inputs.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_invalid_inputs.py::test_invalid_inputs[path0]
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_invalid_inputs.py::test_invalid_inputs[invalid_path]
============================== 2 failed in 0.11s ===============================
"""