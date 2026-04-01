
from pathlib import Path
from typing import Iterator, TextIO

import pytest

from isort.io import File


def test_none_input():
    with pytest.raises(TypeError):
        for file in File.read("example_file.txt"):
            pass
