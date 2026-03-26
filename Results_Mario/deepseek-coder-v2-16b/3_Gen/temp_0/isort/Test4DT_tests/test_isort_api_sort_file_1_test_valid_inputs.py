
import pytest
from pathlib import Path
from isort.api import sort_file as isort_sort_file
from unittest.mock import patch

@pytest.mark.parametrize("filename", [
    "test_file.py",  # A valid file name with .py extension
    Path("test_file.py"),  # A valid Path object for the same file
])
def test_valid_inputs(filename):
    """Test standard input with valid parameters."""
    with patch('sys.stdout', new=open('/dev/null', 'w')):  # Mock stdout to avoid actual output during tests
        result = isort_sort_file(filename)
        assert isinstance(result, bool), "The function should return a boolean value."
