
# Module: isort.api
from isort.api import _tmp_file
import pytest
from pathlib import Path

# Define a sample File class for testing purposes
class File:
    def __init__(self, file_path: str, mode: str, encoding: str):
        self.path = Path(file_path)
        self.mode = mode
        self.encoding = encoding

# Test cases for the _tmp_file function
def test_basic_usage():
    source_file = File("example.txt", 'r', 'utf-8')
    new_temp_file = _tmp_file(source_file)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_api__tmp_file_0.py F.                     [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        source_file = File("example.txt", 'r', 'utf-8')
        new_temp_file = _tmp_file(source_file)
>       assert str(new_temp_file) == "Path('/data/example.isorted')"
E       assert 'example.txt.isorted' == "Path('/data/...ple.isorted')"
E         
E         - Path('/data/example.isorted')
E         + example.txt.isorted

isort/Test4DT_tests/test_isort_api__tmp_file_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__tmp_file_0.py::test_basic_usage - ...
========================= 1 failed, 1 passed in 0.10s ==========================
"""