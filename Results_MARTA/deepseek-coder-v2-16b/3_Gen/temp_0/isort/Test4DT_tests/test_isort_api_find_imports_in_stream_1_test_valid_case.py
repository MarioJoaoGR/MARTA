
from pathlib import Path
from typing import TextIO

import pytest

from isort.api import DEFAULT_CONFIG, Config, find_imports_in_stream

# Sample Python code with imports for testing
sample_code = """
import os
import sys
from some_module import some_function
"""

def test_valid_case():
    # Create a temporary file with the sample code
    with open('example.py', 'w') as f:
        f.write(sample_code)
    
    # Open the created file for reading
    file_path = Path('example.py')
    with open(file_path, 'r') as input_stream:
        # Test the function with the opened file
        imports = list(find_imports_in_stream(input_stream))
    
    # Clean up by removing the temporary file
    Path('example.py').unlink()

    # Assert that the number of imports is as expected
    assert len(imports) == 3, "Expected 3 imports but got {}".format(len(imports))
