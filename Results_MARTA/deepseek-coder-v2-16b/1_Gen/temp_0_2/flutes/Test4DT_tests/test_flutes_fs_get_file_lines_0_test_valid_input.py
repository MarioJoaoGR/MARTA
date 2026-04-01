
import subprocess
from pathlib import Path
import pytest
from flutes.fs import get_file_lines

def test_valid_input():
    # Create a temporary file for testing
    temp_file = Path("temp_test_file.txt")
    with open(temp_file, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    try:
        # Call the function and check the output
        line_count = get_file_lines(temp_file)
        assert line_count == 3
        
        # Check if the file is properly read
        with open(temp_file, 'r') as f:
            content = f.read()
            assert "Line 1\nLine 2\nLine 3\n" in content
    
    finally:
        # Clean up the temporary file
        temp_file.unlink()
