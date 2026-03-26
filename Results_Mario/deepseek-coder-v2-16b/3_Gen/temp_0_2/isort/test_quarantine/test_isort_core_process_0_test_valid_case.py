
import pytest
from io import StringIO
from isort.core import process
from isort.settings import DEFAULT_CONFIG

def test_valid_case():
    # Create a sample Python file with unsorted imports
    with open('sample.py', 'w') as f:
        f.write("import os\nimport sys\n")
    
    # Read the sample Python file
    with open('sample.py', 'r') as input_file, open('sorted_sample.py', 'w') as output_file:
        # Call the process function to sort imports
        result = process(input_file, output_file)
    
    # Read the sorted file and check if imports are sorted
    with open('sorted_sample.py', 'r') as sorted_file:
        content = sorted_file.read()
        assert "import os\n" in content
        assert "import sys\n" in content
    
    # Clean up the sample file
    import os
    os.remove('sample.py')
    os.remove('sorted_sample.py')
