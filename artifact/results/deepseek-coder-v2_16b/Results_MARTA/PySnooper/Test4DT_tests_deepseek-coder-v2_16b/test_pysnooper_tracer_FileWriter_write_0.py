
import pytest
from io import StringIO
import sys
from pysnooper.tracer import FileWriter

# Test for writing to a file when overwrite is True

# Test for appending to a file when overwrite is False
def test_valid_input_append():
    # Create a temporary file for testing
    with open('example.txt', 'w') as f:
        pass  # Ensure the file exists and is empty if overwrite is False
    
    writer = FileWriter('example.txt', False)
    writer.write('Appended text.')
    
    with open('example.txt', 'r') as f:
        content = f.read()
        assert 'Appended text.' in content, f"Expected 'Appended text.' but got {content}"