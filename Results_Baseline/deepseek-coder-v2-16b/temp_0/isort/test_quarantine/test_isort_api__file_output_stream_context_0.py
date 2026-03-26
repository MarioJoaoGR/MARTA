
# Module: isort.api
import pytest
from pathlib import Path
from io import TextIOBase
from typing import Iterator
from unittest.mock import patch
import shutil

# Assuming _tmp_file and File are properly defined elsewhere in your code
def _file_output_stream_context(filename: str | Path, source_file: 'File') -> Iterator[TextIO]:
    tmp_file = _tmp_file(source_file)
    with tmp_file.open("w+", encoding=source_file.encoding, newline="") as output_stream:
        shutil.copymode(filename, tmp_file)
        yield output_stream

# Test cases for _file_output_stream_context function

def test_file_output_stream_context_string_filename():
    # Arrange
    filename = "/path/to/original/file.txt"
    source_file = File(Path("/path/to/original/file.txt"), mode='r', encoding='utf-8')
    
    # Act
    with patch('shutil.copymode') as mock_copymode:
        gen = _file_output_stream_context(filename, source_file)
        temp_file = next(gen)
        
        # Assert
        assert isinstance(temp_file, TextIOBase)
        mock_copymode.assert_called_once_with(filename, Path("/path/to/original/file.txt.isorted"))

def test_file_output_stream_context_path_filename():
    # Arrange
    filename = Path("/path/to/original/file.txt")
    source_file = File(Path("/path/to/original/file.txt"), mode='r', encoding='utf-8')
    
    # Act
    with patch('shutil.copymode') as mock_copymode:
        gen = _file_output_stream_context(filename, source_file)
        temp_file = next(gen)
        
        # Assert
        assert isinstance(temp_file, TextIOBase)
        mock_copymode.assert_called_once_with(filename, Path("/path/to/original/file.txt.isorted"))

def test_file_output_stream_context_invalid_source_file():
    # Arrange
    filename = "/path/to/original/file.txt"
    source_file = None  # Invalid File object
    
    # Act & Assert
    with pytest.raises(TypeError):
        _file_output_stream_context(filename, source_file)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__file_output_stream_context_0
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0.py:11:87: E0602: Undefined variable 'TextIO' (undefined-variable)
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0.py:12:15: E0602: Undefined variable '_tmp_file' (undefined-variable)
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0.py:22:18: E0602: Undefined variable 'File' (undefined-variable)
isort/Test4DT_tests/test_isort_api__file_output_stream_context_0.py:36:18: E0602: Undefined variable 'File' (undefined-variable)


"""