
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File

def test_invalid_file():
    invalid_file = 'invalid_filename'
    with pytest.raises(FileNotFoundError):
        File._open(invalid_file)
