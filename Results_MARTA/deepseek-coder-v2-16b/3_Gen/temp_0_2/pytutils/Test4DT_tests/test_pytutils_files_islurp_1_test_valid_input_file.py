
import pytest
import sys
import os
import functools
from pytutils.files import islurp

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_valid_input_file():
    # Create a temporary file with some content
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    # Test reading from the temporary file
    lines = list(islurp(temp_file_path))
    assert len(lines) == 3
    assert lines[0] == "Line 1\n"
    assert lines[1] == "Line 2\n"
    assert lines[2] == "Line 3"
    
    # Clean up the temporary file
    os.remove(temp_file_path)
