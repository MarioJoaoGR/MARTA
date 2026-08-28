
import pytest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
import os
import functools
from pytutils.files import islurp

def test_reading_local_text_file_line_by_line():
    with patch('builtins.open', create=True) as mock_open:
        expected_lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
        mock_file = MagicMock()
        mock_file.__iter__.return_value = expected_lines
        mock_open.return_value = mock_file

        result = list(islurp('example.txt'))
        assert result == expected_lines

def test_reading_standard_input():
    with patch('sys.stdin', StringIO('\n'.join(['Line 1', 'Line 2', 'Line 3']))):
        result = list(islurp('-', allow_stdin=True))
        assert result == ['Line 1\n', 'Line 2\n', 'Line 3\n']

def test_reading_local_binary_file_chunk_by_chunk():
    with patch('builtins.open', create=True) as mock_open:
        expected_chunks = [b'Chunk1', b'Chunk2', b'Chunk3']
        mock_file = MagicMock()
        mock_file.__iter__.return_value = expected_chunks
        mock_open.return_value = mock_file

        result = list(islurp('binaryfile.bin', mode='rb', iter_by=1024))
        assert result == expected_chunks

def test_reading_from_standard_input_with_specific_iteration_mode():
    with patch('sys.stdin', StringIO('\n'.join(['Line 1', 'Line 2', 'Line 3']))):
        result = list(islurp('-', allow_stdin=True, iter_by=512))
        assert result == ['Line 1\n', 'Line 2\n', 'Line 3\n']

def test_expanding_user_home_directory_and_environment_variables_in_filename():
    with patch('os.path', spec=True) as mock_os_path:
        expected_path = '/expanded/path'
        mock_os_path.expanduser.return_value = expected_path
        mock_os_path.expandvars.return_value = expected_path

        result = list(islurp('~/documents/report.txt', expanduser=True, expandvars=True))
        assert result == ['Line 1\n', 'Line 2\n', 'Line 3\n']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""