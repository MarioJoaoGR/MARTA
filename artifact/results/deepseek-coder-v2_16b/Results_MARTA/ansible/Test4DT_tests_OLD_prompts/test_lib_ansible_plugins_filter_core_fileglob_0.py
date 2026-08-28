
import pytest
from ansible.plugins.filter.core import fileglob
import glob
import os
from unittest.mock import patch, MagicMock

def test_fileglob_basic():
    with patch('glob.glob', return_value=['file1.txt', 'file2.txt']):
        with patch('os.path.isfile', side_effect=[True, True]):
            result = fileglob('*.txt')
            assert result == ['file1.txt', 'file2.txt']

def test_fileglob_no_matches():
    with patch('glob.glob', return_value=[]):
        with patch('os.path.isfile', side_effect=[False]):
            result = fileglob('*.txt')
            assert result == []

def test_fileglob_mixed_files():
    with patch('glob.glob', return_value=['file1.txt', 'dir/file2.txt']):
        with patch('os.path.isfile', side_effect=[True, False]):
            result = fileglob('*.txt')
            assert result == ['file1.txt']
