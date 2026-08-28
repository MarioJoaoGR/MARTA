
import pytest
from semantic_release.settings import _config_from_pyproject
import os
import tomlkit
from tomlkit.exceptions import TOMLKitError



def test_non_toml_file():
    # Arrange
    path = "test/path/to/invalid/file.txt"  # Replace with a real path to a non-TOML file

    # Act
    config = _config_from_pyproject(path)

    # Assert
    assert config == {}, "Expected an empty dictionary for a file that is not TOML."

def test_missing_tool_section():
    # Arrange
    path = "test/path/to/valid/but/missing/tool/pyproject.toml"  # Replace with a real path to a pyproject.toml without 'tool' section

    # Act
    config = _config_from_pyproject(path)

    # Assert
    assert config == {}, "Expected an empty dictionary if the 'tool' section is missing."

def test_missing_semantic_release_section():
    # Arrange
    path = "test/path/to/valid/but/missing/semantic_release/pyproject.toml"  # Replace with a real path to a pyproject.toml without 'tool' > 'semantic_release' section

    # Act
    config = _config_from_pyproject(path)

    # Assert
    assert config == {}, "Expected an empty dictionary if the 'tool' > 'semantic_release' section is missing."