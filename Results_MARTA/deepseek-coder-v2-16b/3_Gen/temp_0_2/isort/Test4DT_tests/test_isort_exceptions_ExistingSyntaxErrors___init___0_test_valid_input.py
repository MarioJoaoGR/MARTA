
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_valid_input():
    # Define a valid file path (this could be a mock or an actual file)
    valid_file_path = "tests/test_file.py"
    
    # Attempt to instantiate the exception with a valid file path
    try:
        raise ExistingSyntaxErrors(valid_file_path)
    except ExistingSyntaxErrors as e:
        assert e.file_path == valid_file_path
