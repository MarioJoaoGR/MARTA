
import pytest
from unittest.mock import MagicMock
from pathlib import Path
from typing import Iterator, TextIO
import shutil

# Assuming _file_output_stream_context is defined in a module named 'isort.api'
from isort.api import _file_output_stream_context

@pytest.fixture
def mock_source_file():
    source_file = MagicMock()
    source_file.path = Path("/path/to/data.txt")
    source_file.encoding = "utf-8"
    return source_file

@pytest.fixture
def mock_filename():
    return "/path/to/data.txt"

def test_valid_input(mock_source_file, mock_filename):
    # Call the function under test
    result = list(_file_output_stream_context(mock_filename, mock_source_file))
    
    # Assertions to verify the behavior
    assert len(result) == 1
    output_stream = result[0]
    assert isinstance(output_stream, TextIO)
    assert output_stream.mode == 'w+'
    assert output_stream._name == str(mock_source_file.path.with_suffix(".isorted"))
    
    # Verify that the permissions were copied correctly (this would typically require additional checks based on platform and file system)
    shutil.copymode(mock_filename, mock_source_file.path.with_suffix(".isorted"))

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

isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mock_source_file = <MagicMock id='139658843486800'>
mock_filename = '/path/to/data.txt'

    def test_valid_input(mock_source_file, mock_filename):
        # Call the function under test
>       result = list(_file_output_stream_context(mock_filename, mock_source_file))
E       TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_input.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""