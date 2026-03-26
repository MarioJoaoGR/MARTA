
from pathlib import Path
import pytest
from isort.io import File

@pytest.mark.parametrize("filename", [None, "test_file.txt"])
def test_none_input(filename):
    with pytest.raises(TypeError):
        for file in File.read(filename):
            pass
