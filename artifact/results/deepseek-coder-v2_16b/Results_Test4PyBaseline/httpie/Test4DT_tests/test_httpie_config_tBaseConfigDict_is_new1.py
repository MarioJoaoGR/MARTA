
import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

# Test initialization with a valid file path
def test_baseconfigdict_initialization():
    config = BaseConfigDict(path=Path('/valid/file/path'))
    assert isinstance(config, BaseConfigDict)
    assert config.path == Path('/valid/file/path')
    assert config.name is None
    assert config.helpurl is None

# Test the `is_new` method with a non-existent file path
def test_baseconfigdict_is_new_non_existent():
    config = BaseConfigDict(path=Path('/nonexistent/file/path'))
    assert config.is_new() is True

# Test the `is_new` method with an existing file path
def test_baseconfigdict_is_new_existing():
    temp_file = Path('/tmp/somefile')
    temp_file.touch()  # Create an empty file at the path
    config = BaseConfigDict(path=temp_file)
    assert config.is_new() is False

# Test the `is_new` method with a directory instead of a file
def test_baseconfigdict_is_new_directory():
    temp_dir = Path('/tmp/somedir')
    temp_dir.mkdir(exist_ok=True)  # Create a directory at the path, ignore if it already exists
    config = BaseConfigDict(path=temp_dir)