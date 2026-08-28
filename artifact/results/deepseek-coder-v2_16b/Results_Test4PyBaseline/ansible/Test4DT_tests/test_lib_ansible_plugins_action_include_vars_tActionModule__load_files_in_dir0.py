# Module: ansible.plugins.action.include_vars
import pytest
from ansible.plugins.action import ActionModule as Am
import os

@pytest.fixture
def action_module():
    return Am()

# Test loading files from a directory with default settings
def test_load_files_in_dir_default(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'])
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"

# Test loading files with a specific depth
def test_load_files_in_dir_with_depth(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'], depth=1)
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"

# Test loading files matching a specific pattern
def test_load_files_in_dir_with_pattern(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'], files_matching=r'^.*\.yaml$')
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"

# Test ignoring specific files
def test_load_files_in_dir_with_ignore(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'], ignore_files=['ignore_me\.yaml'])
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"

# Test specifying file extensions to load
def test_load_files_in_dir_with_extensions(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'], extensions=['yaml'])
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"

# Test ignoring unknown file extensions
def test_load_files_in_dir_with_ignore_unknown(action_module):
    result = action_module._load_files_in_dir('/path/to/root', ['file1.yaml', 'file2.yml'], ignore_unknown_extensions=True)
    assert not result[0], "Expected no failure, but got one"
    assert isinstance(result[2], dict), "Expected a dictionary as the result of loaded files"
