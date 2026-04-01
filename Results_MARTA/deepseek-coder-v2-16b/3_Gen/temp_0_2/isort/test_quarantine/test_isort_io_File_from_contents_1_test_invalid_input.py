
import pytest
from io import StringIO, BytesIO
from pathlib import Path
from isort.io import File

def test_invalid_input():
    contents = 123
    filename = "example_file.txt"
    
    with pytest.raises(TypeError):
        File.from_contents(contents, filename)

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

isort/Test4DT_tests/test_isort_io_File_from_contents_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        contents = 123
        filename = "example_file.txt"
    
        with pytest.raises(TypeError):
>           File.from_contents(contents, filename)

isort/Test4DT_tests/test_isort_io_File_from_contents_1_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

contents = 123, filename = 'example_file.txt'

    @staticmethod
    def from_contents(contents: str, filename: str) -> "File":
>       encoding = File.detect_encoding(filename, BytesIO(contents.encode("utf-8")).readline)
E       AttributeError: 'int' object has no attribute 'encode'

isort/isort/io.py:32: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_from_contents_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""