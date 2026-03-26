
import pytest
from pathlib import Path
from isort.api import check_file

@pytest.fixture(scope="module")
def sample_file():
    # Create a temporary file with some sample Python code for testing
    content = """import os
import sys
"""
    temp_file_path = "sample_code.py"
    with open(temp_file_path, 'w') as f:
        f.write(content)
    yield temp_file_path
    # Clean up the temporary file after the test
    Path(temp_file_path).unlink()

def test_check_file_valid_input(sample_file):
    assert check_file(sample_file, show_diff=False) is True
