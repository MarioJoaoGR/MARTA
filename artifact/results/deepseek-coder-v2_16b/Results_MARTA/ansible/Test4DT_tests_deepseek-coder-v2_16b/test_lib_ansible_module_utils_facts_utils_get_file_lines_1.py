
import pytest
from ansible.module_utils.facts.utils import get_file_lines

def test_get_file_lines_valid_path():
    # Test retrieving lines from a valid file path
    result = get_file_lines('example.txt')
    assert isinstance(result, list), "Expected a list of strings"
    assert len(result) > 0, "Expected non-empty list for a valid file"


def test_get_file_lines_strip_whitespace():
    # Test retrieving lines and ensuring whitespace is stripped
    result = get_file_lines('example_with_spaces.txt', strip=True)
    assert all(line.strip() == line for line in result), "Expected all lines to be stripped of whitespace"
