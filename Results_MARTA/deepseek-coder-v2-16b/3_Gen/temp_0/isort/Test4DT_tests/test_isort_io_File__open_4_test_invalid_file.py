
from io import TextIOWrapper
from pathlib import Path

import pytest

from isort.io import File


def test_invalid_file():
    invalid_file = 'invalid_filename'
    with pytest.raises(FileNotFoundError):
        File._open(invalid_file)
