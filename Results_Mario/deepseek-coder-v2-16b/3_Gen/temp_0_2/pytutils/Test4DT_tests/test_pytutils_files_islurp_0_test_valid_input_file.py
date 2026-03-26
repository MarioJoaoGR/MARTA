
import os
import sys
import tempfile
import pytest
from unittest.mock import patch

# Assuming 'islurp' is defined in a module named 'pytutils.files'
from pytutils.files import islurp

@pytest.fixture(scope="module")
def valid_file():
    # Create a temporary text file with multiple lines of content
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, 'test_file.txt')
    with open(temp_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    yield temp_file_path
    # Clean up the temporary file after the test
    os.remove(temp_file_path)

def test_valid_input_file(valid_file):
    with patch('sys.stdin', open(valid_file)):
        lines = list(islurp(valid_file))
        assert len(lines) == 3
        assert lines[0] == "Line 1\n"
        assert lines[1] == "Line 2\n"
        assert lines[2] == "Line 3\n"
