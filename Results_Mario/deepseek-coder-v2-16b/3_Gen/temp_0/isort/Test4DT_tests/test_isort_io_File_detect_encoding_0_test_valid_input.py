
import pytest
from isort.io import File
from io import TextIOBase
from pathlib import Path
from tokenize import detect_encoding, TokenError
from unittest.mock import Mock

def test_valid_input():
    # Create a mock for the readline function
    mock_readline = Mock()
    mock_readline.side_effect = [b'coding=utf-8\n', b'', b'']  # Simulate reading lines from the file

    # Call the detect_encoding method with a valid filename and mock readline
    detected_encoding = File.detect_encoding("example_file.txt", mock_readline)
    
    # Assert that the encoding is correctly detected
    assert detected_encoding == "utf-8"
