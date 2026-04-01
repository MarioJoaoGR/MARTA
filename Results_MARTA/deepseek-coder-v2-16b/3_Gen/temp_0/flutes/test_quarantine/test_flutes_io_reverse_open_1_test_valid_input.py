
import io
from pathlib import Path
from flutes.io import reverse_open
import pytest

@pytest.mark.parametrize("test_file, test_encoding, test_allow_empty_lines, test_buffer_size", [
    ('example.txt', 'utf-8', True, io.DEFAULT_BUFFER_SIZE)
])
def test_valid_input(test_file, test_encoding, test_allow_empty_lines, test_buffer_size):
    path = Path(test_file)
    with reverse_open(path, encoding=test_encoding, allow_empty_lines=test_allow_empty_lines, buffer_size=test_buffer_size) as f:
        lines = list(f)
        assert len(lines) > 0, "The file should have at least one line"
        for line in lines:
            assert isinstance(line, str), "Each line should be a string"
