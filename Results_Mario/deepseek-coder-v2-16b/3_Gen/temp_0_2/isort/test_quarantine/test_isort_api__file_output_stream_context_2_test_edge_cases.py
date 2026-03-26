
from pathlib import Path
import shutil
from typing import Iterator, TextIO
from unittest.mock import patch
import pytest
from isort.api import _file_output_stream_context
from tempfile import NamedTemporaryFile

@pytest.fixture
def mock_source_file():
    source_file = type('File', (), {'path': Path('/some/file'), 'encoding': 'utf-8'})()
    return source_file

@pytest.fixture
def mock_filename():
    return '/some/file'

def test_isort_api__file_output_stream_context(mock_source_file, mock_filename):
    with patch('shutil.copymode') as copymode_mock:
        with patch('builtins.open', create=True) as open_mock:
            open_mock.return_value.__enter__.return_value = NamedTemporaryFile(mode='w+', delete=False)
            
            result = list(_file_output_stream_context(mock_filename, mock_source_file))
            
            assert len(result) == 1
            open_mock.assert_called_once_with(any(), 'w+', encoding='utf-8', newline="")
            copymode_mock.assert_called_once_with(mock_filename, any())

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

isort/Test4DT_tests/test_isort_api__file_output_stream_context_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________ test_isort_api__file_output_stream_context __________________

mock_source_file = <Test4DT_tests.test_isort_api__file_output_stream_context_2_test_edge_cases.File object at 0x7f7130b7b590>
mock_filename = '/some/file'

    def test_isort_api__file_output_stream_context(mock_source_file, mock_filename):
        with patch('shutil.copymode') as copymode_mock:
            with patch('builtins.open', create=True) as open_mock:
                open_mock.return_value.__enter__.return_value = NamedTemporaryFile(mode='w+', delete=False)
    
>               result = list(_file_output_stream_context(mock_filename, mock_source_file))
E               TypeError: '_GeneratorContextManager' object is not iterable

isort/Test4DT_tests/test_isort_api__file_output_stream_context_2_test_edge_cases.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__file_output_stream_context_2_test_edge_cases.py::test_isort_api__file_output_stream_context
============================== 1 failed in 0.14s ===============================
"""