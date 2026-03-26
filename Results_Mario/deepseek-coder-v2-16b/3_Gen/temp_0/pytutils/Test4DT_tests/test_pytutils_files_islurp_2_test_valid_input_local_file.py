
import os
import sys
import tempfile
import pytest
from pytutils.files import islurp

@pytest.fixture(scope="module")
def create_temp_file():
    # Create a temporary text file with multiple lines
    content = "Line 1\nLine 2\nLine 3\n"
    temp_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp_file.write(content)
    temp_file.close()
    yield temp_file.name
    os.remove(temp_file.name)

def test_valid_input_local_file(create_temp_file):
    with open(create_temp_file, 'r') as f:
        expected_lines = [line for line in f.readlines()]
    
    lines = list(islurp(create_temp_file))
    
    assert lines == expected_lines
