
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File

def test_invalid_file_path():
    with pytest.raises(Exception):
        File._open("nonexistent_file.txt")
