
import pytest
from ansible.module_utils.facts.utils import get_file_lines
import os


def test_get_file_lines_default_stripping():
    # Test retrieving lines from an existing file with default stripping behavior
    expected_lines = ["line1", "line2", "line3"]
    with open("test_file.txt", "w") as f:
        for line in expected_lines:
            f.write(line + "\n")
    
    result = get_file_lines('test_file.txt')
    assert result == expected_lines, f"Expected {expected_lines}, but got {result}"
    os.remove("test_file.txt")

def test_get_file_lines_custom_separator():
    # Test retrieving lines from an existing file with a custom separator
    content = "line1,line2,line3"
    with open("test_file.csv", "w") as f:
        f.write(content)
    
    expected_lines = ["line1", "line2", "line3"]
    result = get_file_lines('test_file.csv', line_sep=',')
    assert result == expected_lines, f"Expected {expected_lines}, but got {result}"
    os.remove("test_file.csv")

def test_get_file_lines_no_stripping():
    # Test retrieving lines from an existing file without stripping whitespace
    content = " line1\n line2\n line3"
    with open("test_file.txt", "w") as f:
        f.write(content)
    
    expected_lines = [" line1", " line2", " line3"]
    result = get_file_lines('test_file.txt', strip=False)
    assert result == expected_lines, f"Expected {expected_lines}, but got {result}"
    os.remove("test_file.txt")