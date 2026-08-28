
import pytest
from unittest.mock import patch, MagicMock
import os
import io
from ansible.executor.discovery.python_target import read_utf8_file

def test_read_valid_utf8_file():
    with patch('os.access', return_value=True), \
         patch('io.open', side_effect=[io.StringIO("Valid UTF-8 content")]):
        result = read_utf8_file('/path/to/valid_file.txt')
        assert result == "Valid UTF-8 content"


def test_read_non_existent_file():
    with patch('os.access', return_value=False):
        result = read_utf8_file('/path/to/nonexistent_file.txt')
        assert result is None