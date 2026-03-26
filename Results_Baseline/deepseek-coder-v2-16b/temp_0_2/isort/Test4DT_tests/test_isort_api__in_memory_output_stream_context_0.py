
from io import StringIO, TextIOBase
from typing import Iterator, TextIO

import pytest

# Import the function from its module
from isort.api import _in_memory_output_stream_context


def test__in_memory_output_stream_context():
    # Arrange
    expected_output = "First line.\nSecond line."
    
    # Act
    with _in_memory_output_stream_context() as mem_stream:
        print("First line.", file=mem_stream)
        print("Second line.", file=mem_stream)
        
        # Read the output from the in-memory stream
        captured_output = mem_stream.getvalue().strip()  # Added .strip() to remove any trailing newline characters
    
    # Assert
    assert captured_output == expected_output
