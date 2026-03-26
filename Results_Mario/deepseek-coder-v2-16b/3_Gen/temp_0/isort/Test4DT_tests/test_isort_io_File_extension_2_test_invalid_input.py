
import os
from pathlib import Path
from typing import TextIO

import pytest


class File:
    stream: TextIO
    path: Path
    encoding: str
    
    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")
        self.stream = open(file_path, mode, encoding=encoding)
        self.encoding = encoding
    
    def extension(self) -> str:
        return self.path.suffix.lstrip(".")

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        file = File('nonexistent.txt')
