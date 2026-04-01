
import pytest
from pathlib import Path
from flutes.io import reverse_open
import io

@pytest.mark.parametrize("path, encoding, allow_empty_lines, buffer_size", [
    (Path('example.txt'), 'utf-8', False, io.DEFAULT_BUFFER_SIZE),
    (Path('example.txt'), 'latin-1', True, 16384)
])
def test_valid_input(path, encoding, allow_empty_lines, buffer_size):
    reversed_file = reverse_open(path, encoding=encoding, allow_empty_lines=allow_empty_lines, buffer_size=buffer_size)
    assert reversed_file is not None
