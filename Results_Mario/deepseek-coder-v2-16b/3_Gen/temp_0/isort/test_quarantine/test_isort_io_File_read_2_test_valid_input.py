
import pytest
from pathlib import Path
from isort.io import File

def test_valid_input():
    # Create a temporary file with some content
    temp_file_path = Path("temp_test_file.txt")
    temp_file_content = "This is a test line.\nAnother line here."
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write(temp_file_content)
    
    # Test reading the file
    files = list(File.read(temp_file_path))
    
    assert len(files) == 2
    for file in files:
        assert isinstance(file, File)
        assert file.stream is not None
        assert file.path == temp_file_path
        assert file.encoding == 'utf-8'

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

isort/Test4DT_tests/test_isort_io_File_read_2_test_valid_input.py F      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a temporary file with some content
        temp_file_path = Path("temp_test_file.txt")
        temp_file_content = "This is a test line.\nAnother line here."
        with open(temp_file_path, 'w', encoding='utf-8') as f:
            f.write(temp_file_content)
    
        # Test reading the file
>       files = list(File.read(temp_file_path))
E       TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_io_File_read_2_test_valid_input.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_read_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""