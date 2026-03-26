
from isort.io import File
import pytest
from pathlib import Path
from typing import Iterator, TextIO

def test_none_input():
    with pytest.raises(TypeError):
        for file in File.read("example_file.txt"):
            pass
