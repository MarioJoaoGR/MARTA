
from pathlib import Path
from typing import TextIO

import pytest


class File:
    stream: TextIO
    path: Path
    encoding: str

    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path) if file_path else None
        self.stream = open(file_path, mode, encoding=encoding) if file_path else None
        self.encoding = encoding

    def extension(self) -> str:
        return self.path.suffix.lstrip(".") if self.path else None

@pytest.fixture
def file():
    return File(None)

def test_edge_case(file):
    assert file.extension() is None
