
import pytest
from isort.api import _file_output_stream_context
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Iterator, TextIO
import shutil

@pytest.fixture
def source_file():
    # Create a temporary file for the source content
    with NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("This is a test content.")
        tmp.seek(0)
        yield tmp

@pytest.fixture
def filename():
    return "test_file.txt"

def test_invalid_input(source_file, filename):
    with pytest.raises(TypeError):
        list(_file_output_stream_context(filename, source_file))
