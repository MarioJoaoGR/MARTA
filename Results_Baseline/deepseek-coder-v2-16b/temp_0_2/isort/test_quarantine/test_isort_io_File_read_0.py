
# Module: isort.io
# test_isort_io.py
from pathlib import Path
import pytest
from io import StringIO
from contextlib import nullcontext as does_not_raise
from unittest.mock import patch, mock_open
from isort.io import File

@pytest.fixture(params=[Path("example.txt"), "example.txt"])
def file_path(request):
    return request.param

@pytest.fixture
def example_file():
    content = ["line1\n", "line2\n", "line3\n"]
    mock_file = mock_open(read_data="".join(content))
    with patch("builtins.open", mock_file):
        yield mock_file, content

def test_read_from_path():
    path = Path("example.txt")
    expected_lines = ["line1\n", "line2\n", "line3\n"]
    with patch("builtins.open", mock_open(read_data="".join(expected_lines))):
        files = list(File.read(path))
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

isort/Test4DT_tests/test_isort_io_File_read_0.py F                       [100%]

=================================== FAILURES ===================================
_____________________________ test_read_from_path ______________________________

    def test_read_from_path():
        path = Path("example.txt")
        expected_lines = ["line1\n", "line2\n", "line3\n"]
        with patch("builtins.open", mock_open(read_data="".join(expected_lines))):
>           files = list(File.read(path))
E           TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_io_File_read_0.py:26: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_read_0.py::test_read_from_path
============================== 1 failed in 0.10s ===============================
"""