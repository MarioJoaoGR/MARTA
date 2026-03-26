
import pytest
from pathlib import Path
from flutes.io import progress_open

@pytest.mark.parametrize("path", [Path('valid_file.bin')])
def test_valid_input(path):
    with pytest.raises(FileNotFoundError):
        reader = progress_open(path, mode='rb')
