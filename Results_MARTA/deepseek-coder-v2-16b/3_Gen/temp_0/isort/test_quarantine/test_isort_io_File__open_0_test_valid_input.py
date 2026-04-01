
from pathlib import Path
import pytest
from isort.io import File

@pytest.fixture
def valid_file():
    return Path("test_file.txt")

def test_valid_input(valid_file):
    with File._open(valid_file) as f:
        assert f.readable()
