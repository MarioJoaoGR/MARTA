
import pytest
from pathlib import Path
from typing import TextIO
from isort.io import File

@pytest.fixture
def sample_file(tmp_path):
    # Create a temporary file with some content for testing
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Sample content", encoding="utf-8")
    return File(file_path, open(file_path, "r", encoding="utf-8"), "utf-8")

def test_valid_input(sample_file):
    assert sample_file.extension() == "txt"

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

isort/Test4DT_tests/test_isort_io_File_extension_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

sample_file = File(stream=PosixPath('/tmp/pytest-of-joaovitorino/pytest-47/test_valid_input0/test_file.txt'), path=<_io.TextIOWrappe...e='/tmp/pytest-of-joaovitorino/pytest-47/test_valid_input0/test_file.txt' mode='r' encoding='utf-8'>, encoding='utf-8')

    def test_valid_input(sample_file):
>       assert sample_file.extension() == "txt"

isort/Test4DT_tests/test_isort_io_File_extension_5_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = File(stream=PosixPath('/tmp/pytest-of-joaovitorino/pytest-47/test_valid_input0/test_file.txt'), path=<_io.TextIOWrappe...e='/tmp/pytest-of-joaovitorino/pytest-47/test_valid_input0/test_file.txt' mode='r' encoding='utf-8'>, encoding='utf-8')

    @property
    def extension(self) -> str:
>       return self.path.suffix.lstrip(".")
E       AttributeError: '_io.TextIOWrapper' object has no attribute 'suffix'

isort/isort/io.py:37: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File_extension_5_test_valid_input.py::test_valid_input
============================== 1 failed in 0.13s ===============================
"""