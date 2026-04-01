
from pathlib import Path
from typing import TextIO
from unittest.mock import patch, MagicMock
import pytest

class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path)
        try:
            self.stream = open(file_path, mode, encoding=encoding)
        except FileNotFoundError:
            self.stream = None
        self.encoding = encoding
        
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

def test_edge_case():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            file = File('non_existent_file.txt')

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

isort/Test4DT_tests/test_isort_io_File_extension_1_test_edge_case.py F   [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('builtins.open', side_effect=FileNotFoundError):
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_io_File_extension_1_test_edge_case.py:25: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_extension_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""