
from unittest.mock import MagicMock

import pytest

from isort.api import _tmp_file  # Assuming the function is in the api module


def test_none_input():
    # Create a mock File object with a path attribute
    source_file = MagicMock()
    source_file.path = MagicMock()
    source_file.path.suffix = ".txt"  # Example suffix
    
    # Mock the behavior of the path object to return a specific string when called
    expected_path_str = "/path/to/original/file.txt.isorted"
    source_file.path.with_suffix.return_value.__str__.return_value = expected_path_str
    
    # Call the function under test
    result = _tmp_file(source_file)
    
    # Assert that the returned path has the correct suffix
    assert str(result) == expected_path_str
