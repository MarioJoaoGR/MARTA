
import pytest
from pathlib import Path
from flutils.pathutils import directory_present

# Test cases for directory_present function

def test_directory_present_basic():
    # Ensure a directory exists at the specified path
    result = directory_present('~/tmp/test_path')
    assert isinstance(result, Path)