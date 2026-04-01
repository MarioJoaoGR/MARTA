
import pytest
from io import StringIO, BytesIO
from pathlib import Path
from unittest.mock import patch
from isort.io import File

def test_file_from_contents():
    # Test content and filename
    contents = "example content"
    filename = "example_file.txt"
    
    with patch('isort.io.File.detect_encoding') as mock_detect_encoding:
        # Mock the return value of detect_encoding
        mock_detect_encoding.return_value = 'utf-8'
        
        # Call the method under test
        file = File.from_contents(contents, filename)
        
        # Assertions to verify the output
        assert isinstance(file, File)
        assert file.stream is not None
        assert file.path == Path(filename).resolve()
        assert file.encoding == 'utf-8'
