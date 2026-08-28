
import pytest
import os
import tomlkit
from semantic_release.settings import _config_from_pyproject



def test_non_toml_file():
    # Arrange
    path = "test/path/to/a/file/that/is/not/toml.txt"  # Replace with a real path to a non-TOML file
    
    # Act
    config = _config_from_pyproject(path)
    
    # Assert
    assert config == {}, "Expected an empty dictionary for a file that is not in TOML format."

def test_non_existent_file():
    # Arrange
    path = "nonexistent/path/to/pyproject.toml"  # Replace with a non-existent path
    
    # Act
    config = _config_from_pyproject(path)
    
    # Assert
    assert config == {}, "Expected an empty dictionary for a non-existent file."