
import pytest
from unittest.mock import MagicMock
from pathlib import Path

# Assuming _tmp_file is defined in your module or script
def _tmp_file(source_file: 'File') -> Path:
    return source_file.path.with_suffix(source_file.path.suffix + ".isorted")

class File:
    def __init__(self, path):
        self.path = Path(path)

@pytest.fixture
def valid_file():
    mock_file = MagicMock()
    mock_file.path = Path('/path/to/original/file.txt')
    return mock_file

def test_valid_input(valid_file):
    result = _tmp_file(valid_file)
    assert result == Path('/path/to/original/file.txt.isorted')
