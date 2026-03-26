
import pytest
from pathlib import Path
from typing import TextIO

class File:
    stream: TextIO
    path: Path
    encoding: str

    def __init__(self, file_path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = Path(file_path) if file_path else None
        if file_path:
            self.stream = open(file_path, mode, encoding=encoding)
        else:
            self.stream = None
        self.encoding = encoding

    def extension(self) -> str:
        return self.path.suffix.lstrip(".") if self.path else None

@pytest.fixture
def file_instance():
    yield File(None)

def test_edge_case(file_instance):
    assert file_instance.extension() is None
