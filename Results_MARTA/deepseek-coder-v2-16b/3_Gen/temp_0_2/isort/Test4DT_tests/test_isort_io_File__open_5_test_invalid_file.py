
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File  # Correcting the import to match the provided code

def test_invalid_file():
    with pytest.raises(Exception):
        File._open("nonexistent_file.txt")
