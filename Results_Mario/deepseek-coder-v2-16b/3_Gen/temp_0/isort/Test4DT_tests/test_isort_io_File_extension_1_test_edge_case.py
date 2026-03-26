
from pathlib import Path
from typing import TextIO
import pytest
from unittest.mock import patch, MagicMock

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

def test_edge_case():
    with patch('builtins.open', side_effect=FileNotFoundError):
        file_path = 'nonexistentfile.txt'
        with pytest.raises(FileNotFoundError):
            File(file_path)
