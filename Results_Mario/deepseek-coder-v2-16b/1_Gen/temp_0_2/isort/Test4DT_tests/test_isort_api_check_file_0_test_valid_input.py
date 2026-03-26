
import pytest
from pathlib import Path
from isort.api import check_file

# Assuming the function `check_file` expects a valid file path, we need to create a mock or fixture that provides such a path.
@pytest.fixture
def good_file():
    # Create a temporary test file with known good content for testing
    good_content = """import os
import sys
"""
    temp_file_path = Path("tests/good_file.py")
    temp_file_path.write_text(good_content)
    yield str(temp_file_path)  # Provide the path as a string to the function under test
    # Clean up: remove the temporary file after the test is done
    temp_file_path.unlink()

def test_valid_input(good_file):
    result = check_file(good_file)
    assert result is True, f"Expected `check_file` to return `True` for a valid file but got {result}"
