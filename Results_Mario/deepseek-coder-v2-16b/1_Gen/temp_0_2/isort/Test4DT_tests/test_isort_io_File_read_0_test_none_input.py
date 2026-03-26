
import pytest
from pathlib import Path
from isort.io import File

@pytest.mark.parametrize("filename", [None, ""])
def test_none_input(filename):
    with pytest.raises(TypeError):
        list(File.read(filename))
