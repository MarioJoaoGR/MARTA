
import pytest
from pytutils.files import burp
import os
import sys
from unittest.mock import patch, MagicMock

def test_burp_write_to_file():
    with patch('builtins.open', create=True) as mock_open:
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        burp('example.txt', 'Hello, world!')
        
        mock_open.assert_called_with('example.txt', 'w')
        mock_file.write.assert_called_with('Hello, world!')

def test_burp_write_to_stdout():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        burp('-', 'Hello, world!', allow_stdout=True)
        
        mock_stdout.write.assert_called_with('Hello, world!')


