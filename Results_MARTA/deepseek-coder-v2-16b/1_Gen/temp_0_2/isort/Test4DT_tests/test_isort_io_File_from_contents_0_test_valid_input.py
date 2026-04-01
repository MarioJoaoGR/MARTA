
from unittest.mock import patch, MagicMock
from io import StringIO, BytesIO
from pathlib import Path
import pytest
from isort.io import File  # Correcting the import to match the function's module

def test_valid_input():
    contents = "This is a test file."
    filename = "example_file.txt"
    
    with patch('isort.io.File.detect_encoding', return_value='utf-8'):
        file = File.from_contents(contents, filename)
        
        assert isinstance(file, File)
        assert file.stream.read() == contents
        assert file.path == Path(filename).resolve()
        assert file.encoding == 'utf-8'
