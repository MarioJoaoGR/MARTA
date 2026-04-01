
import pytest
from pathlib import Path
from isort.api import Config, sort_file
from io import StringIO

@pytest.fixture
def mock_config():
    return Config()

def test_sort_file(mock_config):
    # Create a temporary file for testing
    temp_file = "temp_test_file.py"
    with open(temp_file, 'w') as f:
        f.write("import os\nimport sys\n")
    
    # Test the function with the mock config
    result = sort_file(temp_file, config=mock_config)
    
    # Read the file after sorting to check if it's sorted correctly
    with open(temp_file, 'r') as f:
        content = f.read()
    
    assert "import sys\n" in content  # Ensure sys is imported before os
    assert "import os\n" in content   # After sorting, os should be after sys
    
    # Clean up the temporary file
    Path(temp_file).unlink()
