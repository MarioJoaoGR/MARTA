# Module: apimd.loader
import os
import pytest
from apimd.loader import _write

def test_write_to_new_file(tmp_path):
    """Test writing to a new file."""
    file_path = tmp_path / "newfile.txt"
    content = "Hello, World!"
    _write(str(file_path), content)
    
    assert file_path.exists()
    with open(file_path, 'r', encoding='utf-8') as f:
        assert f.read() == content

def test_write_to_existing_file(tmp_path):
    """Test overwriting an existing file."""
    file_path = tmp_path / "existingfile.txt"
    initial_content = "Initial content."
    _write(str(file_path), initial_content)
    
    new_content = "Overwritten content."
    _write(str(file_path), new_content)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        assert f.read() == new_content

def test_write_markdown_content(tmp_path):
    """Test writing Markdown formatted content."""
    file_path = tmp_path / "markdown.md"
    markdown_content = """
# Sample Documentation

## Introduction
This document serves as an example of how to use the _write function.
"""
    _write(str(file_path), markdown_content)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        assert f.read() == markdown_content

def test_write_empty_string(tmp_path):
    """Test writing an empty string."""
    file_path = tmp_path / "emptyfile.txt"
    _write(str(file_path), "")
    
    assert file_path.exists()
    with open(file_path, 'r', encoding='utf-8') as f:
        assert f.read() == ""

def test_write_with_special_characters(tmp_path):
    """Test writing content with special characters."""
    file_path = tmp_path / "specialchars.txt"
    special_content = "Special characters: @#$%^&*()"
    _write(str(file_path), special_content)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        assert f.read() == special_content

def test_write_non_string_content(tmp_path):
    """Test writing non-string content."""
    file_path = tmp_path / "nonstringfile.txt"
    with pytest.raises(TypeError):
        _write(str(file_path), 12345)  # Passing an integer instead of a string
