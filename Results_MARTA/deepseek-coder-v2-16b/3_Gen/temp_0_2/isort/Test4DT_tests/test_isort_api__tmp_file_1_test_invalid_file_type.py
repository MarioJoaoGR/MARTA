
import pytest
from unittest.mock import MagicMock
from isort.api import _tmp_file  # Assuming this is the correct module for the function

def test_invalid_file_type():
    # Create a mock File class without path attribute
    source_file = MagicMock()
    source_file.path = None  # Simulating no path attribute
    
    with pytest.raises(AttributeError):
        _tmp_file(source_file)
