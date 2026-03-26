
from pathlib import Path

import pytest

from isort.api import DEFAULT_CONFIG, Config, find_imports_in_file

# Define a sample file content with 4 import statements for demonstration purposes
SAMPLE_FILE_CONTENT = """import os
import sys
import time
import math"""

@pytest.fixture
def sample_file():
    # Create a temporary file with the sample content
    temp_file = Path('/tmp/test_file.py')
    temp_file.write_text(SAMPLE_FILE_CONTENT)
    yield temp_file  # Provide the file path to the test function
    # Clean up: remove the temporary file after the test
    temp_file.unlink()

def test_find_imports_in_file_valid(sample_file):
    config = Config()  # Assuming DEFAULT_CONFIG is sufficient for this test
    imports = list(find_imports_in_file(sample_file, config=config))
    assert len(imports) == 4  # Adjusted to match the actual number of imports in SAMPLE_FILE_CONTENT
