
import pytest
from io import StringIO, BytesIO
from pathlib import Path
from unittest.mock import patch
from isort.io import File

@pytest.mark.parametrize("contents, filename", [
    ("example content", "example_file.txt")
])
def test_valid_input(contents, filename):
    with patch('isort.io.File.detect_encoding') as mock_detect_encoding:
        # Mock the return value of detect_encoding
        mock_detect_encoding.return_value = "utf-8"
        
        file = File.from_contents(contents, filename)
        
        assert isinstance(file, File)
        assert file.stream.read() == contents
        assert file.path == Path(filename).resolve()
        assert file.encoding == "utf-8"
