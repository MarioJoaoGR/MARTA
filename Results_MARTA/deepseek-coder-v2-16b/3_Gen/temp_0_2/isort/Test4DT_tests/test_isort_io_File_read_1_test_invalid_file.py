
from pathlib import Path
from typing import Iterator, TextIO
import pytest
from isort.io import File  # Assuming this module contains the File class definition

def test_invalid_file():
    with pytest.raises(Exception):
        list(File.read("nonexistent_file.txt"))
