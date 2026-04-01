
import pytest
from pathlib import Path
from isort.io import File

def test_valid_input():
    filename = "example_file.txt"
    file_content = ["line1\n", "line2\n", "line3\n"]
    
    with open(filename, 'w') as f:
        f.writelines(file_content)
    
    files = list(File.read(filename))
    
    assert len(files) == 3
    for i, file in enumerate(files):
        assert isinstance(file, File)
        assert file.stream.readline() == file_content[i]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_io_File_read_0_test_valid_input.py F      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        filename = "example_file.txt"
        file_content = ["line1\n", "line2\n", "line3\n"]
    
        with open(filename, 'w') as f:
            f.writelines(file_content)
    
>       files = list(File.read(filename))
E       TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_io_File_read_0_test_valid_input.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_read_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""