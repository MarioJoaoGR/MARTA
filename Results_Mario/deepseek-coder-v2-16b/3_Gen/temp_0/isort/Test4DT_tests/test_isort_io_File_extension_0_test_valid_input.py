
from pathlib import Path
from typing import TextIO
from unittest.mock import mock_open, patch

import pytest


class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path)
        self.stream = open(file_path, mode, encoding=encoding)
        self.encoding = encoding
    
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

def test_valid_input():
    with patch('builtins.open', mock_open(read_data='dummy data')):
        file = File('example.txt')
        assert file.extension() == 'txt'
