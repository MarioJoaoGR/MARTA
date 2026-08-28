# Module: apimd.loader
import pytest
from apimd.loader import _read

# Test cases for the _read function

def test_read_existing_file(tmp_path):
    # Create a temporary file and write some content to it
    test_file = tmp_path / "test.txt"
    test_content = "Hello, world!"
    test_file.write_text(test_content)

    # Read the content using the _read function
    assert _read(str(test_file)) == test_content

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty.txt"
    test_file.touch()

    # Read the content using the _read function
    assert _read(str(test_file)) == ""

def test_read_nonexistent_file():
    # Attempt to read a non-existent file
    with pytest.raises(FileNotFoundError):
        _read("non_existent_file.txt")

def test_read_unreadable_file(tmp_path):
    # Create a temporary file and make it unreadable
    test_file = tmp_path / "unreadable.txt"
    test_file.touch()
    test_file.chmod(0o000)  # Remove all permissions

    # Attempt to read the unreadable file
    with pytest.raises(IOError):
        _read(str(test_file))

def test_read_relative_path(tmp_path, monkeypatch):
    # Create a temporary directory and a file within it
    temp_dir = tmp_path / "subdir"
    temp_dir.mkdir()
    test_file = temp_dir / "relative.txt"
    test_content = "Relative path test."
    test_file.write_text(test_content)

    # Change the current working directory to the parent of the temporary directory
    monkeypatch.chdir(tmp_path)

    # Read the content using a relative path
    assert _read(f"subdir/{test_file.name}") == test_content

def test_read_absolute_path(tmp_path):
    # Create a temporary file and write some content to it
    test_file = tmp_path / "absolute.txt"
    test_content = "Absolute path test."
    test_file.write_text(test_content)

    # Read the content using an absolute path
    assert _read(str(test_file)) == test_content
