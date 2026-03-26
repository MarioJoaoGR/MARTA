
from pathlib import Path
from typing import Iterator, TextIO
from unittest.mock import patch, MagicMock
import pytest

# Assuming the File class is defined in the module 'isort.io'
from isort.io import File

@pytest.mark.parametrize("filename", [None])
def test_none_input(filename):
    with pytest.raises(Exception):
        list(File.read(filename))
