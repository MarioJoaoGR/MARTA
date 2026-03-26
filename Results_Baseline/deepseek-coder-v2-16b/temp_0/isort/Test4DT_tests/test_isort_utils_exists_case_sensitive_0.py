
import os
import sys

import pytest

from isort.utils import exists_case_sensitive

# Test cases for exists_case_sensitive function

@pytest.mark.skipif(sys.platform != "win32", reason="This test only applies to Windows")
def test_exists_case_sensitive_windows_existing_file():
    # Arrange
    path = "C:\\path\\to\\existing_file"
    
    # Act
    result = exists_case_sensitive(path)
    
    # Assert
    assert result is True, f"Expected True for existing file on Windows but got {result}"

@pytest.mark.skipif(sys.platform != "win32", reason="This test only applies to Windows")
def test_exists_case_sensitive_windows_non_existing_file():
    # Arrange
    path = "C:\\path\\to\\nonexistent_file"
    
    # Act
    result = exists_case_sensitive(path)
    
    # Assert
    assert result is False, f"Expected False for non-existent file on Windows but got {result}"

@pytest.mark.skipif(sys.platform != "win32", reason="This test only applies to Windows")
def test_exists_case_sensitive_windows_existing_but_wrong_case():
    # Arrange
    path = "C:\\path\\to\\File"
    
    # Act
    result = exists_case_sensitive(path)
    
    # Assert
    assert result is False, f"Expected False for existing file with wrong case on Windows but got {result}"

@pytest.mark.skipif(sys.platform == "win32", reason="This test only applies to non-Windows systems")
def test_exists_case_sensitive_non_windows():
    # Arrange
    path = "/usr/local/bin/script.py"
    
    # Act
    result = exists_case_sensitive(path)
    
    # Assert