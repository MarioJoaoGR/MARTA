
from pathlib import Path
from isort.api import find_imports_in_file
import pytest

@pytest.fixture(scope="module")
def temp_file(tmp_path_factory):
    # Create a temporary file with some Python code that includes imports
    test_code = """
import os
import sys
from datetime import datetime
"""
    temp_file_path = tmp_path_factory.mktemp("test_files") / "test_file.py"
    temp_file_path.write_text(test_code)
    return str(temp_file_path)  # Return the path as a string for the test function

def test_valid_input(temp_file):
    imports = list(find_imports_in_file(temp_file))  # Convert iterator to list for easier assertion
    assert len(imports) > 0, "No imports found in the test file"
