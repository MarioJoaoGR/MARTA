
import pytest
from flutes.io import progress_open
import io
import os

@pytest.mark.parametrize("path", ["non_existent_file.txt"])
def test_invalid_input(path):
    with pytest.raises(FileNotFoundError):
        with progress_open(path, mode="r") as f:
            pass

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

flutes/Test4DT_tests/test_flutes_io_progress_open_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
__________________ test_invalid_input[non_existent_file.txt] ___________________

path = 'non_existent_file.txt'

    @pytest.mark.parametrize("path", ["non_existent_file.txt"])
    def test_invalid_input(path):
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

flutes/Test4DT_tests/test_flutes_io_progress_open_1_test_invalid_input.py:9: Failed
----------------------------- Captured stderr call -----------------------------

  0%|          | [00:00<?]
  0%|          | [00:00<?]
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_1_test_invalid_input.py::test_invalid_input[non_existent_file.txt]
============================== 1 failed in 0.10s ===============================
"""