
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from isort.api import _file_output_stream_context

@pytest.fixture
def mock_source_file():
    # Create a mock source file object
    mock = MagicMock()
    mock.encoding = 'utf-8'  # Example encoding
    return mock

@pytest.fixture
def mock_tmp_file():
    # Create a mock temporary file path
    mock = MagicMock(spec=Path)
    return mock

def test_file_output_stream_context(mock_source_file, mock_tmp_file):
    filename = Path("/path/to/original/file.txt")
    with patch('isort.api._tmp_file', return_value=mock_tmp_file):
        with patch('shutil.copymode') as copymode_mock:
            gen = _file_output_stream_context(filename, mock_source_file)
            output_stream = iter(gen).__next__()  # Convert generator to iterator and get the next item
            assert isinstance(output_stream, MagicMock), "Expected a MagicMock object but got something else"

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

isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________ test_file_output_stream_context ________________________

mock_source_file = <MagicMock id='140506097565520'>
mock_tmp_file = <MagicMock spec='Path' id='140506097472336'>

    def test_file_output_stream_context(mock_source_file, mock_tmp_file):
        filename = Path("/path/to/original/file.txt")
        with patch('isort.api._tmp_file', return_value=mock_tmp_file):
            with patch('shutil.copymode') as copymode_mock:
                gen = _file_output_stream_context(filename, mock_source_file)
>               output_stream = iter(gen).__next__()  # Convert generator to iterator and get the next item
E               TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_edge_case.py:25: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__file_output_stream_context_0_test_edge_case.py::test_file_output_stream_context
============================== 1 failed in 0.11s ===============================
"""