
from io import BytesIO, StringIO
from pathlib import Path
from typing import TextIO

import pytest

from isort.io import File


# Test cases for the from_contents method of the File class
def test_from_contents_basic():
    # Basic test with a string content and filename
    file = File.from_contents("example content", "example_file.txt")
    assert isinstance(file, File)
    assert file.path == Path("example_file.txt").resolve()
    assert file.encoding == "utf-8"