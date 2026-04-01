
import io
from pathlib import Path
from unittest.mock import patch
from isort.api import check_file, Config, DEFAULT_CONFIG

def test_check_file_valid_input():
    # Define a temporary file for testing
    temp_file = "temp_test_script.py"
    
    # Write some sample Python code to the temporary file
    with open(temp_file, 'w') as f:
        f.write("import os\n")
        f.write("import sys\n")
    
    try:
        # Test the function with valid input
        result = check_file(temp_file)
        
        # Assert that the function returns True since no issues are expected
        assert result is True
        
    finally:
        # Clean up by deleting the temporary file
        Path(temp_file).unlink()
